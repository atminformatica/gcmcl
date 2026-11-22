from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.http import HttpResponse

from django.contrib.auth.models import User 

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class GcmListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Gcm
    template_name = 'gcm_list.html'
    context_object_name = 'gcms'
    paginate_by = 10
    permission_required = 'gcms.view_gcm'

    def get_queryset(self):
        queryset = super().get_queryset()
        pesquisar_nome = self.request.GET.get('pesquisar_nome')
        pesquisar_cpf = self.request.GET.get('pesquisar_cpf')
        pesquisar_identidade = self.request.GET.get('pesquisar_identidade')
        pesquisar_matricula = self.request.GET.get('pesquisar_matricula')
        
        if pesquisar_nome:
            queryset = queryset.filter(nome__icontains=pesquisar_nome)                   
            
        if pesquisar_cpf:
            queryset = queryset.filter(cpf__icontains=pesquisar_cpf)                   
            
        if pesquisar_identidade:
            queryset = queryset.filter(identidade__icontains=pesquisar_identidade)                   
            
        if pesquisar_matricula:
            queryset = queryset.filter(matricula__icontains=pesquisar_matricula)                   
            
        return queryset
    
    #esse metodo permite adicionar mais dados ao contexto da view
    #que sera enviado para a  template html
    #vamos adicionar as categorias e marcas
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuarios'] = User.objects.all()

        return context

class GcmCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Gcm
    template_name = 'gcm_create.html'
    form_class = forms.GcmForm
    success_url = reverse_lazy('gcm_list')
    permission_required = 'gcm.add_product'

class GcmDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Gcm
    template_name = 'gcm_detail.html'  # Ajuste conforme a pasta dos seus templates
    context_object_name = 'object'         # Padrão do Django (funciona direto com o HTML anterior)
    permission_required = 'gcms.view_gcm'

    def get_queryset(self):
        # Otimiza a consulta trazendo o relacionamento ForeignKey/OneToOne 'user' de uma vez
        return super().get_queryset().select_related('user')

class GcmDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Gcm
    permission_required = 'gcms.delete_gcm'
    success_url = reverse_lazy('gcm_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        # Se for HTMX, retorna vazio para remover a linha da tabela
        if request.headers.get('HX-Request'):
            return HttpResponse("")
        # Se for formulário tradicional (tela de detalhes), redireciona normalmente
        return super().delete(request, *args, **kwargs)

class GcmUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Gcm
    template_name = 'gcm_update.html' 
    form_class = forms.GcmForm
    success_url = reverse_lazy('gcm_list')
    permission_required = 'gcms.change_gcm'