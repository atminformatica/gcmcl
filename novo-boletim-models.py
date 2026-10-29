# from django.db import models
# from django.contrib.auth.models import User 

# class GCM(models.Model):
#     OPCOES_SEXO = [
#         ('MASCULINO', 'Masculino'),
#         ('FEMININO', 'Feminino'),
#     ]
#     OPCOES_ESTADO_CIVIL = [
#         ('SOLTEIRO', 'Solteiro(a)'),
#         ('CASADO', 'Casado(a)'),
#         ('DIVORCIADO', 'Divorciado(a)'),
#         ('VIUVO', 'Viúvo(a)'),
#         ('SEPARADO', 'Separado(a) judicialmente'),
#         ('UNIAO_ESTAVEL', 'União Estável'),
#     ]

#     # CRIA O RELACIONAMENTO DE AUTENTICAÇÃO
#     # Se o gcm for apagado, o perfil do GCM também será (CASCADE)
#     user = models.OneToOneField(
#         User, 
#         on_delete=models.CASCADE, 
#         related_name='gcm_profile',
#         verbose_name='Usuário do Sistema'
#     )
#     nome = models.CharField(max_length=150, verbose_name='NOME')
#     nome_guerra = models.CharField(max_length=50, verbose_name='NOME GUERRA')
#     sexo = models.CharField(max_length=10, choices=OPCOES_SEXO, blank=True, null=True, verbose_name='SEXO')
#     pai = models.CharField(blank=True, null=True, max_length=150, verbose_name='PAI')
#     mae = models.CharField(blank=True, null=True, max_length=150, verbose_name='MÃE')
#     naturalidade = models.CharField(blank=True, null=True, max_length=100, verbose_name='NATURALIDADE')
#     datanascimento = models.DateField(blank=True, null=True,verbose_name='DATA DE NASCIMENTO')    
#     endereco = models.CharField(blank=True, null=True, max_length=150, verbose_name='ENDEREÇO')
#     numero = models.CharField(blank=True, null=True, max_length=10, verbose_name='NÚMERO')
#     bairro = models.CharField(blank=True, null=True, max_length=60, verbose_name='BAIRRO')
#     complemento = models.CharField(blank=True, null=True, max_length=60, verbose_name='COMPLEMENTO')
#     cidade = models.CharField(blank=True, null=True, max_length=60, verbose_name='CIDADE')
#     uf = models.CharField(blank=True, null=True, max_length=2, verbose_name='UF')
#     cep = models.CharField(blank=True, null=True, max_length=9, verbose_name='CEP')
#     telefone = models.CharField(blank=True, null=True, max_length=15, verbose_name='TELEFONE')
#     estadocivil = models.CharField(
#         max_length=20, 
#         choices=OPCOES_ESTADO_CIVIL, 
#         blank=True, 
#         null=True,
#         verbose_name='ESTADO CIVIL',
#         default='SOLTEIRO'
#     )
#     ocupacao_atual = models.CharField(blank=True, null=True, max_length=100,verbose_name='OCUPAÇÃO ATUAL')
#     cpf = models.CharField(blank=True, null=True, max_length=14, unique=True, verbose_name='CPF')
#     cnh = models.CharField(blank=True, null=True, max_length=25, unique=True, verbose_name='CNH')
#     cnh_vencimento = models.DateField(blank=True, null=True,verbose_name='VENCIMENTO CNH') 
#     identidade = models.CharField(blank=True, null=True, max_length=20, verbose_name='IDENTIDADE')
#     orgao_expedidor = models.CharField(blank=True, null=True, max_length=15, verbose_name='ORGÃO EXPEDIDOR')
#     tipo_sangue = models.CharField(blank=True, null=True, max_length=15, verbose_name='TIPO SANGUE')
#     email = models.EmailField(blank=True, null=True, verbose_name='EMAIL')
#     escolaridade = models.CharField(blank=True, null=True, max_length=50, verbose_name='ESCOLARIDADE')
#     cursos = models.TextField(blank=True, null=True, verbose_name='CURSOS')

#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-Hora cadastro')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-Hora atualizado')

#     class Meta:
#         verbose_name = "GCM"
#         verbose_name_plural = "GCMs"

#     def __str__(self):
#         return self.nome


# class Envolvido(models.Model):
#     OPCOES_SEXO = [
#         ('MASCULINO', 'Masculino'),
#         ('FEMININO', 'Feminino'),
#     ]
#     OPCOES_ESTADO_CIVIL = [
#         ('SOLTEIRO', 'Solteiro(a)'),
#         ('CASADO', 'Casado(a)'),
#         ('DIVORCIADO', 'Divorciado(a)'),
#         ('VIUVO', 'Viúvo(a)'),
#         ('SEPARADO', 'Separado(a) judicialmente'),
#         ('UNIAO_ESTAVEL', 'União Estável'),
#     ]
#     nome = models.CharField(max_length=150, verbose_name='NOME')
#     sexo = models.CharField(max_length=10, choices=OPCOES_SEXO, blank=True, null=True, verbose_name='SEXO')
#     pai = models.CharField(blank=True, null=True, max_length=150, verbose_name='PAI')
#     mae = models.CharField(blank=True, null=True, max_length=150, verbose_name='MÃE')
#     naturalidade = models.CharField(blank=True, null=True, max_length=100, verbose_name='NATURALIDADE')
#     datanascimento = models.DateField(blank=True, null=True,verbose_name='DATA DE NASCIMENTO')    
#     endereco = models.CharField(blank=True, null=True, max_length=150, verbose_name='ENDEREÇO')
#     numero = models.CharField(blank=True, null=True, max_length=10, verbose_name='NÚMERO')
#     bairro = models.CharField(blank=True, null=True, max_length=60, verbose_name='BAIRRO')
#     complemento = models.CharField(blank=True, null=True, max_length=60, verbose_name='COMPLEMENTO')
#     cidade = models.CharField(blank=True, null=True, max_length=60, verbose_name='CIDADE')
#     uf = models.CharField(blank=True, null=True, max_length=2, verbose_name='UF')
#     cep = models.CharField(blank=True, null=True, max_length=9, verbose_name='CEP')
#     telefone = models.CharField(blank=True, null=True, max_length=15, verbose_name='TELEFONE')
#     estadocivil = models.CharField(
#         max_length=20, 
#         choices=OPCOES_ESTADO_CIVIL, 
#         blank=True, 
#         null=True,
#         verbose_name='ESTADO CIVIL',
#         default='SOLTEIRO'
#     )
#     ocupacao_atual = models.CharField(blank=True, null=True, max_length=100,verbose_name='OCUPAÇÃO ATUAL')
#     cpf = models.CharField(blank=True, null=True, max_length=14, verbose_name='CPF')
#     identidade = models.CharField(blank=True, null=True, max_length=20, verbose_name='IDENTIDADE')
#     orgao_expedidor = models.CharField(blank=True, null=True, max_length=15, verbose_name='ORGÃO EXPEDIDOR')
#     email = models.EmailField(blank=True, null=True, verbose_name='EMAIL')
#     escolaridade = models.CharField(blank=True, null=True, max_length=50, verbose_name='ESCOLARIDADE')

#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-Hora cadastro')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-Hora atualizado')
#     def __str__(self):
#         return self.nome


# class Veiculo(models.Model):
#     OPCOES_CATEGORIA = [
#         ('AUTOMÓVEL', 'Automóvel'),
#         ('MOTOCICLETA', 'Motocicleta'),
#         ('MOTO ELETRICA ATE 1000W', 'Moto elétrica até 1000w'),
#         ('CAMINHONETE', 'Caminhonete'),
#         ('CAMINHÃO', 'Caminhão'),
#         ('ÔNIBUS', 'Ônibus'),
#         ('MICRO-ÔNIBUS', 'Micro-Ônibus'),
#         ('REBOQUE', 'Reboque'),
#         ('BICICLETA', 'Bicicleta'),
#         ('OUTRO', 'Outro'),
#     ]
#     categoria = models.CharField(max_length=30, choices=OPCOES_CATEGORIA,default='AUTOMÓVEL', verbose_name='CATEGORIA')
#     placa = models.CharField(blank=True, null=True, max_length=8, verbose_name='PLACA')
#     cor = models.CharField(blank=True, null=True, max_length=20, verbose_name='COR')
#     chassi = models.CharField(blank=True, null=True, max_length=17, verbose_name='CHASSI')
#     numero_motor = models.CharField(blank=True, null=True, max_length=30, verbose_name='NÚMERO DO MOTOR')
#     situacao_veiculo = models.CharField(blank=True, null=True, max_length=50,verbose_name='SITUAÇÃO DO VEÍCULO') 
#     avarias = models.CharField(blank=True, null=True, max_length=150, verbose_name='AVARIAS')
#     observacoes = models.TextField(blank=True, null=True, verbose_name='OBSERVAÇÕES') 
#     uf = models.CharField(blank=True, null=True, max_length=2, verbose_name='UF')

#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-Hora cadastro')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-Hora atualizado')   
#     def __str__(self):
#         return self.placa if self.placa else f"{self.chassi} ({self.numero_motor})"


# class Boletim(models.Model):
#     OPCOES_STATUS = [
#         ('EM ANDAMENTO', 'Em Andamento'),
#         ('FINALIZADA', 'Finalizada'),
#     ]
#     OPCOES_ACIONAMENTO = [
#         ('CENTRAL DE COMUNICAÇOES', 'Central de comunicação'),
#         ('DIRETAMENTE AO GUARDA', 'Diretamente ao Guarda'),
#         ('DENUNCIA ANONIMA', 'Denúncia anônima'),
#         ('DEPARANDO COM O FATO', 'Deparando com o fato'),
#         ('INICIATIVA', 'Iniciativa'),
#     ]
#     OPCOES_BOLETIM = [
#         ('BOLETIM DE OCORRENCIA', 'Boletim de Ocorrência'),
#         ('BOLETIM DE INTERVENÇÃO', 'Boletim de Intervenção'),
#     ]
    
#     tipo_boletim = models.CharField(max_length=30, choices=OPCOES_BOLETIM, default='BOLETIM DE INTERVENÇÃO',verbose_name='TIPO DE BOLETIM')
#     status = models.CharField(max_length=30, choices=OPCOES_STATUS, default='EM ANDAMENTO', verbose_name='STATUS')
#     numero_boletim = models.CharField(max_length=15, verbose_name='Boletim Nº')
#     numero_folha = models.CharField(max_length=6, verbose_name='FOLHA Nº')
    
#     destinatario = models.CharField(blank=True, null=True, max_length=255, verbose_name='DESTINATÁRIO') 
#     data_emissao = models.DateField(blank=True, null=True, verbose_name='DATA EMISSÃO')
#     numero_reds = models.CharField(blank=True, null=True, max_length=25, verbose_name='NÚMERO REDS')
    
#     tipificacao_ocorrencia = models.CharField(blank=True, null=True, max_length=100, verbose_name='TIPIFICAÇÃO DA OCORRÊNCIA')
# #-----DO FATO ------------------------------------------------------------------------------
#     acionamento = models.CharField(max_length=30, choices=OPCOES_ACIONAMENTO, default='CENTRAL DE COMUNICAÇOES', verbose_name='ACIONAMENTO')
#     data_hora_inicio = models.DateTimeField(blank=True, null=True, verbose_name='DATA-HORA INÍCIO')
#     data_hora_acionamento = models.DateTimeField(blank=True, null=True, verbose_name='DATA-HORA ACIONAMENTO')
#     data_hora_final = models.DateTimeField(blank=True, null=True, verbose_name='DATA-HORA FINAL')

#     descricao_natureza = models.CharField(blank=True, null=True, max_length=150, verbose_name='DESCRIÇÃO NATUREZA')
#     orgao = models.CharField(blank=True, null=True, max_length=100, verbose_name='ÓRGÃO')
#     setor = models.CharField(blank=True, null=True, max_length=100, verbose_name='SETOR')   

#     endereco_dofato = models.CharField(blank=True, null=True, max_length=255, verbose_name='ENDEREÇO')
#     numero_dofato = models.CharField(blank=True, null=True, max_length=20, verbose_name='NÚMERO')
#     complemento = models.CharField(blank=True, null=True, max_length=100, verbose_name='COMPLEMENTO')
#     bairro_dofato = models.CharField(blank=True, null=True, max_length=100, verbose_name='BAIRRO')
#     cidade_dofato = models.CharField(blank=True, null=True, max_length=100, verbose_name='CIDADE')
#     uf_dofato = models.CharField(blank=True, null=True, max_length=2, verbose_name='UF')
    
# #-----------ENVOLVIDOS------------OUTRA TABELA-------------------------------------------------   
# #-----------VEICULOS--------------OUTRA TABELA-------------------------------------------------   
    
# #-----------HIOSTORICO ------------------------------------------------------------------------   
#     historico = models.TextField(blank=True, null=True, verbose_name='HISTÓRICO')

# #----------- RELATOR --------------------------------------------------------------------------
#     # Agora aponta diretamente para o modelo GCM cadastrado
#     relatornome = models.ForeignKey(
#         'GCM', 
#         on_delete=models.PROTECT, 
#         related_name='boletins_relatados', 
#         verbose_name='RELATOR',
#         blank=True, 
#         null=True
#     )
#     # relatorcargo e relator documento será preenchido automaticamente via HTMX no template
#     relatorcargo = models.CharField(blank=True, null=True, max_length=50, verbose_name='CARGO DO RELATOR')
#     relatordocumento = models.CharField(blank=True, null=True, max_length=50, verbose_name='DOCUMENTO DO RELATOR')
#     coordenar_turno = models.ForeignKey(
#         'GCM', 
#         on_delete=models.PROTECT, 
#         related_name='boletins_coordenados', 
#         verbose_name='COORDENADOR DO TURNO',
#         blank=True, 
#         null=True
#     )
    
# #------------AUTORIDADE ----------------------------------------------------------------------    
#     autoridadenome = models.CharField(blank=True, null=True, max_length=255, verbose_name='AUTORIDADE')
#     autoridadedocumento = models.CharField(blank=True, null=True, max_length=50, verbose_name='DOCUMENTO DA AUTORIDADE')
#     data_recebimento_autoridade = models.DateField(blank=True, null=True, verbose_name='DATA RECEBIMENTO')

# # RELACIONAMENTOS MANY-TO-MANY EXPLICITOS------------------------------------------------------
#     envolvidos = models.ManyToManyField(Envolvido, through='BoletimEnvolvimento', related_name='boletins_envolvido', verbose_name='ENVOLVIDOS')
#     veiculos = models.ManyToManyField(Veiculo, through='BoletimVeiculo', related_name='boletins_veiculo', verbose_name='VEÍCULOS')
    
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-Hora cadastro')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-Hora atualizado')

#     def __str__(self):
#         return f"{self.tipo_boletim} NÚMERO: {self.numero_boletim}"


# class BoletimEnvolvimento(models.Model):
#     TIPOS_ENVOLVIMENTO = [
#         ('SOLICITANTE', 'Solicitante'),
#         ('VITIMA', 'Vítima'),
#         ('AUTOR', 'Autor'),
#         ('TESTEMUNHA', 'Testemunha'),
#         ('SOCORRIDO', 'Socorrado/Vítima'),
#         ('CONDUTOR', 'Condutor'),
#         ('OUTRO', 'Outro'),
#     ]
#     OPCOES_RESPOSTA = [
#         ('SIM', 'SIM'),
#         ('NÃO', 'NÃO'),
#     ]
#     # Adicionado related_name para facilitar consultas reversas
#     boletim = models.ForeignKey(Boletim, on_delete=models.CASCADE, related_name='envolvimentos', verbose_name='BOLETIM')
#     envolvido = models.ForeignKey(Envolvido, on_delete=models.CASCADE, related_name='participacoes', verbose_name='ENVOLVIDO')
    
#     tipo_envolvimento = models.CharField(max_length=30, choices=TIPOS_ENVOLVIMENTO, verbose_name='TIPO DE ENVOLVIMENTO')
#     conduzido_delegacia = models.CharField(max_length=3, choices=OPCOES_RESPOSTA, default='NÃO', verbose_name='CONDUZIDO Á DELEGACIA')
#     resistencia_abordagem = models.CharField(max_length=3, choices=OPCOES_RESPOSTA, default='NÃO', verbose_name='RESISTÊNCIA À ABORDAGEM')
#     uso_algemas = models.CharField(max_length=3, choices=OPCOES_RESPOSTA, default='NÃO', verbose_name='USO DE ALGEMAS')
    
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-Hora cadastro')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-Hora atualizado')
#     class Meta:
#         # Garante que um envolvido só apareça UMA vez por boletim
#         constraints = [
#             models.UniqueConstraint(fields=['boletim', 'envolvido'], name='unique_boletim_envolvido')
#         ]
#     def __str__(self):
#         return f"{self.envolvido.nome} - {self.get_tipo_envolvimento_display()} no Boletim {self.boletim.numero_boletim}"


# class BoletimVeiculo(models.Model):
#     OPCOES_PROCEDIMENTO = [
#         ('APREENDIDO', 'Apreendido'),
#         ('RETIDO', 'Retido'),
#         ('REMOVIDO', 'Removido'),
#         ('LIBERADO NO LOCAL', 'Liberado nolLocal'),
#         ('APENAS ENVOLVIDO', 'Apenas envolvido'),
#     ]
#     # Tabela intermediária para os Veículos (0 a N)
#     # Explicando: o related_name instala uma propriedade na tabela de destino 
#     # apontando de volta para a tabela intermediária:
#     # [ BoletimVeiculo ] 
#     # ├── Campo "boletim" ───(Leva o nome para o destino)───> [ Boletim ] ganha: .veiculos_associados
#     # └── Campo "veiculo" ───(Leva o nome para o destino)───> [ Veiculo ] ganha: .historico_boletins
#     boletim = models.ForeignKey(Boletim, on_delete=models.CASCADE, related_name='veiculos_associados', verbose_name='BOLETIM')
#     veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='historico_boletins', verbose_name='VEÍCULO')
#     procedimento_adotado = models.CharField(max_length=30, choices=OPCOES_PROCEDIMENTO, default='APENAS ENVOLVIDO',verbose_name='PROCEDIMENTO ADOTADO')

#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-Hora cadastro')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-Hora atualizado')
#     class Meta:
#         # Garante que um veículo só seja adicionado UMA vez por boletim
#         constraints = [
#             models.UniqueConstraint(fields=['boletim', 'veiculo'], name='unique_boletim_veiculo')
#         ]
#     def __str__(self):
#         return f"Veículo {self.veiculo.placa} no Boletim {self.boletim.numero_boletim}"
