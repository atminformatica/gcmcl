from django.contrib import admin
from .models import Gcm

@admin.register(Gcm)
class GcmAdmin(admin.ModelAdmin):
    # Colunas exibidas na listagem principal
    list_display = ('nome_guerra', 'nome', 'cpf', 'telefone', 'tipo_sangue', 'cnh_vencimento')
    
    # Campos clicáveis que abrem o registo
    list_display_links = ('nome_guerra', 'nome')
    
    # Barra de pesquisa (busca por nome, nome de guerra, CPF ou utilizador)
    search_fields = ('nome', 'nome_guerra', 'cpf', 'cnh', 'user__username')
    
    # Filtros na barra lateral direita
    list_filter = ('sexo', 'estadocivil', 'tipo_sangue', 'uf')
    
    # Campo de busca rápida para associar o User (útil se houver muitos utilizadores)
    raw_id_fields = ('user',)
    
    # Campos apenas de leitura
    readonly_fields = ('created_at', 'updated_at')

    # Organização dos campos em secções no formulário de edição
    fieldsets = (
        ('Acesso ao Sistema', {
            'fields': ('user',)
        }),
        ('Identificação Pessoal', {
            'fields': (
                ('nome', 'nome_guerra'),
                ('sexo', 'datanascimento', 'estadocivil'),
                ('pai', 'mae'),
                ('naturalidade', 'tipo_sangue'),
            )
        }),
        ('Documentação', {
            'fields': (
                ('cpf', 'identidade', 'orgao_expedidor'),
                ('cnh', 'matricula', 'cnh_vencimento'),
            )
        }),
        ('Contacto e Endereço', {
            'fields': (
                ('telefone', 'email'),
                ('cep', 'endereco', 'numero'),
                ('complemento', 'bairro'),
                ('cidade', 'uf'),
            )
        }),
        ('Dados Profissionais e Formação', {
            'fields': ('ocupacao_atual', 'escolaridade', 'cursos')
        }),
        ('Registos do Sistema', {
            'classes': ('collapse',),  # Secção recolhida por defeito
            'fields': (('created_at', 'updated_at'),)
        }),
    )
