from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from . import models, forms
from gcms.models import Gcm
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse

class BoletimListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Boletim
    template_name = 'boletim_list.html'
    context_object_name = 'boletins'
    paginate_by = 10
    permission_required = 'boletim.view_boletim'

    def get_queryset(self):
        queryset = super().get_queryset()

        # 1. Filtra apenas os boletins onde o usuário logado é o GCM relator
        gcm_logado = getattr(self.request.user, 'gcm_profile', None)
        if not gcm_logado:
            return queryset.none()

        queryset = (
            queryset
            .filter(relatorgcm=gcm_logado)
            .prefetch_related('envolvimentos', 'veiculos_associados', 'guarnicao')
        )

        # 2. Captura e limpa os parâmetros de pesquisa
        pesquisar_nome_envolvido = self.request.GET.get('pesquisar_nome_envolvido', '').strip()
        pesquisar_placa = self.request.GET.get('pesquisar_placa', '').strip()
        pesquisar_numero_boletim = self.request.GET.get('pesquisar_numero_boletim', '').strip()        
        pesquisar = self.request.GET.get('pesquisar', '').strip()

        if pesquisar:
            # Limpa traços/pontos caso o usuário digite placa (ABC-1234) ou CPF (123.456.789-00)
            termo_limpo = pesquisar.replace('-', '').replace('.', '').replace(' ', '')
            queryset = queryset.filter(
            Q(numero_boletim__icontains=pesquisar) |
            Q(numero_reds__icontains=pesquisar) |
            Q(tipificacao_ocorrencia__icontains=pesquisar) |
            Q(endereco_dofato__icontains=pesquisar) |
            Q(bairro_dofato__icontains=pesquisar) |
            Q(envolvidos__nome__icontains=pesquisar) |
            Q(envolvidos__cpf__icontains=termo_limpo) |
            Q(veiculos__placa__icontains=termo_limpo)
        )

        if pesquisar_nome_envolvido:
            queryset = queryset.filter(envolvidos__nome__icontains=pesquisar_nome_envolvido)

        if pesquisar_placa:
            # Remove traço e espaços para bater com o formato salvo no banco (ex: ABC1D23)
            placa_limpa = pesquisar_placa.replace('-', '').replace(' ', '')
            queryset = queryset.filter(veiculos__placa__icontains=placa_limpa)

        if pesquisar_numero_boletim:
            queryset = queryset.filter(numero_boletim__icontains=pesquisar_numero_boletim)
        

        # 3. .distinct() evita repetir o mesmo card se houver 2 envolvidos/veículos parecidos no mesmo BO
        return queryset.distinct()

class BoletimDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Boletim
    permission_required = 'boletim.delete_boletim'
    success_url = reverse_lazy('boletim_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        # Se for HTMX, retorna vazio para remover a linha da tabela
        if request.headers.get('HX-Request'):
            return HttpResponse("")
        # Se for formulário tradicional (tela de detalhes), redireciona normalmente
        return super().delete(request, *args, **kwargs)

class BoletimDetailView(LoginRequiredMixin, DetailView):
    model = models.Boletim
    template_name = 'boletim_detail.html'
    context_object_name = 'boletim'

    def get_queryset(self):
        return (
            models.Boletim.objects
            .select_related('relatorgcm', 'coordenar_turno')
            .prefetch_related(
                'guarnicao',
                'envolvimentos__envolvido',
                'veiculos_associados__veiculo',
            )
        )

class BoletimIniciarView(LoginRequiredMixin, View):
    # Cria o BI em andamento (sem número boletim ainda) e abre direto a tela de edição.
    def get(self, request, *args, **kwargs):
        gcm_logado = getattr(request.user, 'gcm_profile', None)

        boletim = models.Boletim.objects.create(
            status='EM_ANDAMENTO',
            data_hora_inicio=timezone.now(),
            relatorgcm=gcm_logado,
            relator_ocupacao_atual=gcm_logado.ocupacao_atual if gcm_logado else '',
            relator_documento=gcm_logado.matricula if gcm_logado else '',
        )
        return redirect('boletim_update', pk=boletim.pk)

class BoletimUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Boletim
    form_class = forms.BoletimForm
    template_name = 'boletim_update.html'
    permission_required = 'boletim.change_boletim'
    success_url = reverse_lazy('boletim_list')

    def get_queryset(self):
        gcm_logado = getattr(self.request.user, 'gcm_profile', None)
        if not gcm_logado:
            return models.Boletim.objects.none()

        # Só permite editar se estiver EM_ANDAMENTO e pertencer ao GCM logado
        return super().get_queryset().filter(
            relatorgcm=gcm_logado,
            status='EM_ANDAMENTO'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['envolvimentos'] = self.object.envolvimentos.select_related('envolvido').all()
        context['veiculos_associados'] = self.object.veiculos_associados.select_related('veiculo').all()
        return context

    def form_valid(self, form):
        acao = self.request.POST.get('acao')

        if acao == 'finalizar':
            # Valida se o número do BI (CICON) foi preenchido antes de finalizar
            if not form.cleaned_data.get('numero_boletim'):
                form.add_error('numero_boletim', 'Informe o Nº do Boletim (CICON) antes de finalizar.')
                return self.form_invalid(form)

            form.instance.status = 'FINALIZADA'
            messages.success(self.request, 'Boletim finalizado com sucesso!')
            super().form_valid(form)
            return redirect('boletim_list', pk=self.object.pk)

        # Se clicou em "Salvar Rascunho"
        form.instance.status = 'EM_ANDAMENTO'
        messages.success(self.request, 'Boletim salvo com sucesso!')

        return super().form_valid(form)
    
    # usamos esse meto poque precisamos passar a pk para a rota update por 
    # issao nao usamos o success_url = reverse_lazy('boletim_list')
    # def get_success_url(self):
    #     return reverse_lazy('boletim_update', kwargs={'pk': self.object.pk})

class BoletimCancelarView(LoginRequiredMixin, View):
    # """Apaga o boletim APENAS se nunca foi salvo e não tem envolvidos/veículos.
    # Caso contrário, preserva o progresso e apenas volta para a lista."""
    def post(self, request, pk, *args, **kwargs):
        boletim = get_object_or_404(models.Boletim, pk=pk)

        ja_foi_salvo = (boletim.updated_at - boletim.created_at).total_seconds() > 1
        tem_vinculos = boletim.envolvimentos.exists() or boletim.veiculos_associados.exists()

        if ja_foi_salvo or tem_vinculos:
            # Preserva o que o GCM já preencheu e apenas sai da tela
            messages.info(request, 'Edição cancelada pelo usuário.')
        else:
            # Nunca foi salvo e não tem nada vinculado: descarta do banco
            boletim.delete()
            messages.info(request, 'Boletim vazio foi descartado.')

        response = HttpResponse(status=204)
        response['HX-Redirect'] = reverse('boletim_list')
        return response


class BoletimGuarnicaoModalView(LoginRequiredMixin, View):
    """Carrega o conteúdo do modal e também responde à busca em tempo real."""
    def get(self, request, pk, *args, **kwargs):
        boletim = get_object_or_404(models.Boletim, pk=pk)
        termo = request.GET.get('q', '').strip()

        # Busca GCMs ativos (ajuste o filtro se seu model Gcm tiver campo 'ativo')
        gcms = Gcm.objects.all().order_by('nome_guerra')

        if termo:
            gcms = gcms.filter(
                Q(nome_guerra__icontains=termo) |
                Q(nome__icontains=termo) |
                Q(matricula__icontains=termo)
            )

        # Limita a 20 resultados para ficar rápido no celular
        gcms = gcms[:20]
        ids_na_guarnicao = set(boletim.guarnicao.values_list('id', flat=True))

        context = {
            'boletim': boletim,
            'gcms': gcms,
            'ids_na_guarnicao': ids_na_guarnicao,
            'termo': termo,
        }

        # Se a requisição veio do input de busca dentro do modal, retorna só a tabela
                # Troque o if do HX-Target por este:
        if 'q' in request.GET:
            return render(request, 'partials/tabela_busca_guarnicao.html', context)

        # if request.headers.get('HX-Target') == 'tabela-resultados-guarnicao':
        #     return render(request, 'partials/tabela_busca_guarnicao.html', context)

        return render(request, 'partials/modal_guarnicao.html', context)


class BoletimGuarnicaoAdicionarView(LoginRequiredMixin, View):
    permission_required = 'boletim.change_boletim'
    """Adiciona o GCM ao boletim e atualiza tanto o botão no modal quanto a lista na tela principal."""
    def post(self, request, pk, gcm_id, *args, **kwargs):
        boletim = get_object_or_404(models.Boletim, pk=pk)
        gcm = get_object_or_404(Gcm, pk=gcm_id)

        boletim.guarnicao.add(gcm)

        context = {
            'boletim': boletim,
            'gcm': gcm,
            'ja_adicionado': True,
        }
        return render(request, 'partials/resposta_adicionar_guarnicao.html', context)


class BoletimGuarnicaoRemoverView(LoginRequiredMixin, View):
    """Remove o GCM do boletim e atualiza a lista e o contador na tela principal."""
    def post(self, request, pk, gcm_id, *args, **kwargs):
        boletim = get_object_or_404(models.Boletim, pk=pk)
        gcm = get_object_or_404(Gcm, pk=gcm_id)

        boletim.guarnicao.remove(gcm)

        return render(request, 'partials/lista_guarnicao.html', {'object': boletim})