# app: boletim/forms.py
from django import forms
from . import models


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = models.Veiculo

        fields = [
            'categoria',
            'placa',
            'uf',
            'marca_modelo',
            'cor',
            'ano_fabricacao',
            'ano_modelo',
            'chassi',
            'numero_motor',
            'situacao_veiculo',
            'avarias',
            'observacoes',
        ]

        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 8}),
            'uf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
            'marca_modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'cor': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_fabricacao': forms.NumberInput(attrs={'class': 'form-control', 'min': 1900, 'max': 2100}),
            'ano_modelo': forms.NumberInput(attrs={'class': 'form-control', 'min': 1900, 'max': 2100}),
            'chassi': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 17}),
            'numero_motor': forms.TextInput(attrs={'class': 'form-control'}),
            'situacao_veiculo': forms.TextInput(attrs={'class': 'form-control'}),
            'avarias': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

        labels = {
            'categoria': 'Categoria',
            'placa': 'Placa',
            'uf': 'UF',
            'marca_modelo': 'Marca / Modelo',
            'cor': 'Cor',
            'ano_fabricacao': 'Ano de Fabricação',
            'ano_modelo': 'Ano do Modelo',
            'chassi': 'Chassi',
            'numero_motor': 'Número do Motor',
            'situacao_veiculo': 'Situação do Veículo',
            'avarias': 'Avarias',
            'observacoes': 'Observações',
        }

    def clean_placa(self):
        placa = self.cleaned_data.get('placa', '')
        return placa.replace('-', '').replace(' ', '').strip().upper()

    def clean_chassi(self):
        chassi = self.cleaned_data.get('chassi', '')
        return chassi.replace(' ', '').strip().upper()


class EnvolvidoForm(forms.ModelForm):
    class Meta:
        model = models.Envolvido

        fields = [
            'nome',
            'sexo',
            'pai',
            'mae',
            'naturalidade',
            'datanascimento',
            'endereco',
            'numero',
            'bairro',
            'complemento',
            'cidade',
            'uf',
            'cep',
            'telefone',
            'estadocivil',
            'ocupacao_atual',
            'cpf',
            'identidade',
            'orgao_expedidor',
            'email',
            'escolaridade',
        ]

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'pai': forms.TextInput(attrs={'class': 'form-control'}),
            'mae': forms.TextInput(attrs={'class': 'form-control'}),
            'naturalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'datanascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'estadocivil': forms.Select(attrs={'class': 'form-select'}),
            'ocupacao_atual': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'identidade': forms.TextInput(attrs={'class': 'form-control'}),
            'orgao_expedidor': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'escolaridade': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'nome': 'Nome Completo',
            'sexo': 'Sexo',
            'pai': 'Pai',
            'mae': 'Mãe',
            'naturalidade': 'Naturalidade',
            'datanascimento': 'Data de Nascimento',
            'endereco': 'Endereço',
            'numero': 'Número',
            'bairro': 'Bairro',
            'complemento': 'Complemento',
            'cidade': 'Cidade',
            'uf': 'UF',
            'cep': 'CEP',
            'telefone': 'Telefone',
            'estadocivil': 'Estado Civil',
            'ocupacao_atual': 'Ocupação Atual',
            'cpf': 'CPF',
            'identidade': 'Identidade (RG)',
            'orgao_expedidor': 'Órgão Expedidor',
            'email': 'E-mail',
            'escolaridade': 'Escolaridade',
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf:
            cpf_limpo = cpf.replace('.', '').replace('-', '').strip()
            return cpf_limpo if cpf_limpo else None
        return None


class BoletimForm(forms.ModelForm):
    class Meta:
        model = models.Boletim

        fields = [
            'tipo_boletim',
            'status',
            'numero_boletim',
            'numero_folha',
            'destinatario',
            'data_emissao',
            'numero_reds',
            'tipificacao_ocorrencia',
            'acionamento',
            'data_hora_inicio',
            'data_hora_acionamento',
            'data_hora_final',
            'descricao_natureza',
            'orgao',
            'setor',
            'endereco_dofato',
            'numero_dofato',
            'complemento',
            'bairro_dofato',
            'cidade_dofato',
            'uf_dofato',
            'historico',
            'relatorgcm',
            'relator_ocupacao_atual',
            'relator_documento',
            'coordenar_turno',
            'guarnicao',
            'autoridadenome',
            'autoridadedocumento',
            'data_recebimento_autoridade',
        ]

        widgets = {
            'tipo_boletim': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'numero_boletim': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_folha': forms.TextInput(attrs={'class': 'form-control'}),
            'destinatario': forms.TextInput(attrs={'class': 'form-control'}),
            'data_emissao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'numero_reds': forms.TextInput(attrs={'class': 'form-control'}),
            'tipificacao_ocorrencia': forms.TextInput(attrs={'class': 'form-control'}),
            'acionamento': forms.Select(attrs={'class': 'form-select'}),
            'data_hora_inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'data_hora_acionamento': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'data_hora_final': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'descricao_natureza': forms.TextInput(attrs={'class': 'form-control'}),
            'orgao': forms.TextInput(attrs={'class': 'form-control'}),
            'setor': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco_dofato': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_dofato': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro_dofato': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade_dofato': forms.TextInput(attrs={'class': 'form-control'}),
            'uf_dofato': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
            'historico': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'relatorgcm': forms.Select(attrs={'class': 'form-select'}),
            'relator_ocupacao_atual': forms.TextInput(attrs={'class': 'form-control'}),
            'relator_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'coordenar_turno': forms.Select(attrs={'class': 'form-select'}),
            'guarnicao': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'autoridadenome': forms.TextInput(attrs={'class': 'form-control'}),
            'autoridadedocumento': forms.TextInput(attrs={'class': 'form-control'}),
            'data_recebimento_autoridade': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }

        labels = {
            'tipo_boletim': 'Tipo de Boletim',
            'status': 'Status',
            'numero_boletim': 'Boletim Nº',
            'numero_folha': 'Folha Nº',
            'destinatario': 'Destinatário',
            'data_emissao': 'Data de Emissão',
            'numero_reds': 'Número REDS',
            'tipificacao_ocorrencia': 'Tipificação da Ocorrência',
            'acionamento': 'Acionamento',
            'data_hora_inicio': 'Data/Hora Início',
            'data_hora_acionamento': 'Data/Hora Acionamento',
            'data_hora_final': 'Data/Hora Final',
            'descricao_natureza': 'Descrição da Natureza',
            'orgao': 'Órgão',
            'setor': 'Setor',
            'endereco_dofato': 'Endereço do Fato',
            'numero_dofato': 'Número',
            'complemento': 'Complemento',
            'bairro_dofato': 'Bairro',
            'cidade_dofato': 'Cidade',
            'uf_dofato': 'UF',
            'historico': 'Histórico da Ocorrência',
            'relatorgcm': 'GCM Relator',
            'relator_ocupacao_atual': 'Cargo do Relator',
            'relator_documento': 'Documento do Relator',
            'coordenar_turno': 'Coordenador do Turno',
            'guarnicao': 'Guarnição / Apoio',
            'autoridadenome': 'Autoridade Recebedora',
            'autoridadedocumento': 'Documento da Autoridade',
            'data_recebimento_autoridade': 'Data de Recebimento',
        }

    def clean_numero_boletim(self):
        numero = self.cleaned_data.get('numero_boletim', '')
        return numero.strip().upper()

    def clean_numero_reds(self):
        reds = self.cleaned_data.get('numero_reds')
        if reds:
            reds_limpo = reds.strip().upper()
            return reds_limpo if reds_limpo else None
        return None


class BoletimEnvolvimentoForm(forms.ModelForm):
    class Meta:
        model = models.BoletimEnvolvimento

        fields = [           
            'tipo_envolvimento',
            'conduzido_delegacia',
            'resistencia_abordagem',
            'uso_algemas',
        ]

        widgets = {
            'tipo_envolvimento': forms.Select(attrs={'class': 'form-select'}),
            'conduzido_delegacia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'resistencia_abordagem': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'uso_algemas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        labels = {
            'tipo_envolvimento': 'Tipo de Envolvimento',
            'conduzido_delegacia': 'Conduzido à Delegacia',
            'resistencia_abordagem': 'Resistência à Abordagem',
            'uso_algemas': 'Uso de Algemas',
        }


class BoletimVeiculoForm(forms.ModelForm):
    class Meta:
        model = models.BoletimVeiculo

        fields = [
            'procedimento_adotado',
        ]

        widgets = {
            'procedimento_adotado': forms.Select(attrs={'class': 'form-select'}),
        }

        labels = {
            'procedimento_adotado': 'Procedimento Adotado',
        }
