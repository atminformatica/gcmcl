from django.db import models
from django.contrib.auth.models import User 

class Gcm(models.Model):
    OPCOES_SEXO = [
        ('MASCULINO', 'Masculino'),
        ('FEMININO', 'Feminino'),
    ]
    OPCOES_ESTADO_CIVIL = [
        ('SOLTEIRO', 'Solteiro(a)'),
        ('CASADO', 'Casado(a)'),
        ('DIVORCIADO', 'Divorciado(a)'),
        ('VIUVO', 'Viúvo(a)'),
        ('SEPARADO', 'Separado(a) judicialmente'),
        ('UNIAO_ESTAVEL', 'União Estável'),
    ]

    # CRIA O RELACIONAMENTO DE AUTENTICAÇÃO
    # Se o gcm for apagado, o perfil do GCM também será (CASCADE)
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='gcm_profile',
        verbose_name='Usuário do Sistema'
    )
    nome = models.CharField(max_length=150, verbose_name='NOME')
    nome_guerra = models.CharField(max_length=50, verbose_name='NOME GUERRA')
    matricula = models.CharField(max_length=15, verbose_name='MATRICULA')
    sexo = models.CharField(max_length=10, choices=OPCOES_SEXO, blank=True, null=True, verbose_name='SEXO')
    pai = models.CharField(blank=True, null=True, max_length=150, verbose_name='PAI')
    mae = models.CharField(blank=True, null=True, max_length=150, verbose_name='MÃE')
    naturalidade = models.CharField(blank=True, null=True, max_length=100, verbose_name='NATURALIDADE')
    datanascimento = models.DateField(blank=True, null=True,verbose_name='DATA DE NASCIMENTO')    
    endereco = models.CharField(blank=True, null=True, max_length=150, verbose_name='ENDEREÇO')
    numero = models.CharField(blank=True, null=True, max_length=10, verbose_name='NÚMERO')
    bairro = models.CharField(blank=True, null=True, max_length=60, verbose_name='BAIRRO')
    complemento = models.CharField(blank=True, null=True, max_length=60, verbose_name='COMPLEMENTO')
    cidade = models.CharField(blank=True, null=True, max_length=60, verbose_name='CIDADE')
    uf = models.CharField(blank=True, null=True, max_length=2, verbose_name='UF')
    cep = models.CharField(blank=True, null=True, max_length=9, verbose_name='CEP')
    telefone = models.CharField(blank=True, null=True, max_length=15, verbose_name='TELEFONE')
    estadocivil = models.CharField(
        max_length=20, 
        choices=OPCOES_ESTADO_CIVIL, 
        blank=True, 
        null=True,
        verbose_name='ESTADO CIVIL',
    )
    ocupacao_atual = models.CharField(blank=True, null=True, max_length=100,verbose_name='OCUPAÇÃO ATUAL')
    cpf = models.CharField(blank=True, null=True, max_length=14, unique=True, verbose_name='CPF')
    cnh = models.CharField(blank=True, null=True, max_length=25, unique=True, verbose_name='CNH')
    cnh_vencimento = models.DateField(blank=True, null=True,verbose_name='VENCIMENTO CNH') 
    identidade = models.CharField(blank=True, null=True, max_length=20, verbose_name='IDENTIDADE')
    orgao_expedidor = models.CharField(blank=True, null=True, max_length=15, verbose_name='ORGÃO EXPEDIDOR')
    tipo_sangue = models.CharField(blank=True, null=True, max_length=15, verbose_name='TIPO SANGUE')
    email = models.EmailField(blank=True, null=True, verbose_name='EMAIL')
    escolaridade = models.CharField(blank=True, null=True, max_length=50, verbose_name='ESCOLARIDADE')
    cursos = models.TextField(blank=True, null=True, verbose_name='CURSOS')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-Hora cadastro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-Hora atualizado')

    class Meta:
        verbose_name = "GCM"
        verbose_name_plural = "GCMs"

    def __str__(self):
        return self.nome
