from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q


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