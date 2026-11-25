from django.contrib import admin
# (Caso você também precise importar o EnvolvidoForm no admin.py no futuro, 
# importe-o pelo nome específico: from .forms import EnvolvidoForm 
# para não sobrescrever o forms do Django).
from django import forms
from django.db import models

from .models import Envolvido, Veiculo, Boletim, BoletimEnvolvimento, BoletimVeiculo


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    # Deixa todos os inputs de texto visualmente em MAIÚSCULO no Admin
    formfield_overrides = {
        models.CharField: {
            'widget': forms.TextInput(attrs={'style': 'text-transform: uppercase;'})
        },
        models.TextField: {
            'widget': forms.Textarea(attrs={'style': 'text-transform: uppercase;'})
        },
    }

    # Colunas exibidas na listagem principal
    list_display = ('placa', 'uf', 'categoria', 'marca_modelo', 'cor', 'chassi', 'situacao_veiculo')

    # Campos clicáveis que abrem o registro
    list_display_links = ('placa', 'marca_modelo')

    # Barra de pesquisa
    search_fields = ('placa', 'chassi', 'numero_motor', 'marca_modelo')

    # Filtros na barra lateral direita
    list_filter = ('categoria', 'uf', 'cor')

    # Campos apenas de leitura
    readonly_fields = ('created_at', 'updated_at')

    # Organização dos campos em seções no formulário de edição
    fieldsets = (
        ('Identificação do Veículo', {
            'fields': (
                ('categoria', 'marca_modelo', 'cor'),
                ('placa', 'uf'),
                ('ano_fabricacao', 'ano_modelo'),
            )
        }),
        ('Numeração e Chassi', {
            'fields': (
                ('chassi', 'numero_motor'),
            )
        }),
        ('Estado e Observações', {
            'fields': (
                'situacao_veiculo',
                'avarias',
                'observacoes',
            )
        }),
        ('Registros do Sistema', {
            'classes': ('collapse',),
            'fields': (('created_at', 'updated_at'),)
        }),
    )


@admin.register(Envolvido)
class EnvolvidoAdmin(admin.ModelAdmin):
    # Deixa todos os inputs de texto (CharField) visualmente em MAIÚSCULO no Admin
    formfield_overrides = {
        models.CharField: {
            'widget': forms.TextInput(attrs={'style': 'text-transform: uppercase;'})
        },
        models.TextField: {
            'widget': forms.Textarea(attrs={'style': 'text-transform: uppercase;'})
        },
    }

    # Colunas exibidas na listagem principal
    list_display = ('nome', 'cpf', 'identidade', 'telefone', 'cidade', 'uf')
    
    # Campos clicáveis que abrem o registro
    list_display_links = ('nome',)
    
    # Barra de pesquisa (busca por nome, CPF, identidade ou nome da mãe)
    search_fields = ('nome', 'cpf', 'identidade', 'mae')
    
    # Filtros na barra lateral direita
    list_filter = ('sexo', 'estadocivil', 'uf', 'cidade')
    
    # Campos apenas de leitura
    readonly_fields = ('created_at', 'updated_at')

    # Organização dos campos em seções no formulário de edição
    fieldsets = (
        ('Identificação Pessoal', {
            'fields': (
                ('nome', 'sexo'),
                ('datanascimento', 'estadocivil'),
                ('pai', 'mae'),
                ('naturalidade', 'escolaridade', 'ocupacao_atual'),
            )
        }),
        ('Documentação', {
            'fields': (
                ('cpf', 'identidade', 'orgao_expedidor'),
            )
        }),
        ('Contato e Endereço', {
            'fields': (
                ('telefone', 'email'),
                ('cep', 'endereco', 'numero'),
                ('complemento', 'bairro'),
                ('cidade', 'uf'),
            )
        }),
        ('Registros do Sistema', {
            'classes': ('collapse',),  # Seção recolhida por padrão
            'fields': (('created_at', 'updated_at'),)
        }),
    )


class BoletimEnvolvimentoInline(admin.TabularInline):
    model = BoletimEnvolvimento
    extra = 1
    autocomplete_fields = ['envolvido']
    fields = ('envolvido', 'tipo_envolvimento', 'conduzido_delegacia', 'resistencia_abordagem', 'uso_algemas')


class BoletimVeiculoInline(admin.TabularInline):
    model = BoletimVeiculo
    extra = 1
    autocomplete_fields = ['veiculo']
    fields = ('veiculo', 'procedimento_adotado')


@admin.register(Boletim)
class BoletimAdmin(admin.ModelAdmin):
    # Deixa todos os inputs de texto visualmente em MAIÚSCULO no Admin
    formfield_overrides = {
        models.CharField: {
            'widget': forms.TextInput(attrs={'style': 'text-transform: uppercase;'})
        },
        models.TextField: {
            'widget': forms.Textarea(attrs={'style': 'text-transform: uppercase;'})
        },
    }

    # Colunas exibidas na listagem principal
    list_display = (
        'numero_boletim',
        'tipo_boletim',
        'status',
        'data_hora_inicio',
        'tipificacao_ocorrencia',
        'bairro_dofato',
        'relatorgcm',
    )

    # Campos clicáveis que abrem o registro
    list_display_links = ('numero_boletim', 'tipificacao_ocorrencia')

    # Barra de pesquisa
    search_fields = (
        'numero_boletim',
        'numero_reds',
        'tipificacao_ocorrencia',
        'endereco_dofato',
        'bairro_dofato',
        'relatorgcm__nome_guerra',
        'relatorgcm__matricula',
    )

    # Filtros na barra lateral direita
    list_filter = ('status', 'tipo_boletim', 'acionamento', 'bairro_dofato', 'data_emissao')

    # Navegação rápida por datas no topo da listagem
    date_hierarchy = 'data_hora_inicio'

    # Duas caixas lado a lado para selecionar os GCMs da guarnição
    filter_horizontal = ('guarnicao',)

    # Busca rápida para Relator e Coordenador (exige search_fields no GcmAdmin, que você já tem!)
    autocomplete_fields = ('relatorgcm', 'coordenar_turno')

    # Tabelas filhas dentro da tela do Boletim
    inlines = [BoletimEnvolvimentoInline, BoletimVeiculoInline]

    # Campos apenas de leitura
    readonly_fields = ('created_at', 'updated_at')

    # Organização dos campos em seções no formulário de edição
    fieldsets = (
        ('Identificação do Boletim', {
            'fields': (
                ('tipo_boletim', 'status'),
                ('numero_boletim', 'numero_folha', 'numero_reds'),
                ('data_emissao', 'destinatario'),
                'tipificacao_ocorrencia',
            )
        }),
        ('Dados e Local do Fato', {
            'fields': (
                ('acionamento', 'descricao_natureza'),
                ('data_hora_inicio', 'data_hora_acionamento', 'data_hora_final'),
                ('orgao', 'setor'),
                ('endereco_dofato', 'numero_dofato', 'complemento'),
                ('bairro_dofato', 'cidade_dofato', 'uf_dofato'),
            )
        }),
        ('Histórico da Ocorrência', {
            'fields': ('historico',)
        }),
        ('Relator, Coordenação e Guarnição', {
            'fields': (
                ('relatorgcm', 'coordenar_turno'),
                ('relator_ocupacao_atual', 'relator_documento'),
                'guarnicao',
            )
        }),
        ('Autoridade Recebedora', {
            'fields': (
                ('autoridadenome', 'autoridadedocumento', 'data_recebimento_autoridade'),
            )
        }),
        ('Registros do Sistema', {
            'classes': ('collapse',),
            'fields': (('created_at', 'updated_at'),)
        }),
    )
