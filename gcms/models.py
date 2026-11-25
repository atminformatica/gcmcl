# • unique=True e db_index=True na matricula
# • null=True removido dos campos de texto não-únicos (mantido apenas nos campos únicos cpf, cnh, matricula e nas datas)
# • on_delete=models.PROTECT no relacionamento com User
# • Normalização automática no save() (limpando pontuação e padronizando maiúsculas 
#         em cpf, cnh, matricula, nome, nome_guerra e uf, além de converter string vazia para None nos campos únicos para evitar erro no PostgreSQL)
# • ordering = ['nome_guerra'] na class Meta

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

    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='gcm_profile',
        verbose_name='Usuário do Sistema'
    )
    nome = models.CharField(max_length=150, verbose_name='NOME')
    nome_guerra = models.CharField(max_length=50, verbose_name='NOME GUERRA')
    matricula = models.CharField(
        max_length=15,
        unique=True,
        db_index=True,
        verbose_name='MATRÍCULA'
    )
    sexo = models.CharField(
        max_length=10,
        choices=OPCOES_SEXO,
        blank=True,
        default='',
        verbose_name='SEXO'
    )
    pai = models.CharField(max_length=150, blank=True, default='', verbose_name='PAI')
    mae = models.CharField(max_length=150, blank=True, default='', verbose_name='MÃE')
    naturalidade = models.CharField(max_length=100, blank=True, default='', verbose_name='NATURALIDADE')
    datanascimento = models.DateField(blank=True, null=True, verbose_name='DATA DE NASCIMENTO')
    endereco = models.CharField(max_length=150, blank=True, default='', verbose_name='ENDEREÇO')
    numero = models.CharField(max_length=10, blank=True, default='', verbose_name='NÚMERO')
    bairro = models.CharField(max_length=60, blank=True, default='', verbose_name='BAIRRO')
    complemento = models.CharField(max_length=60, blank=True, default='', verbose_name='COMPLEMENTO')
    cidade = models.CharField(max_length=60, blank=True, default='', verbose_name='CIDADE')
    uf = models.CharField(max_length=2, blank=True, default='', verbose_name='UF')
    cep = models.CharField(max_length=9, blank=True, default='', verbose_name='CEP')
    telefone = models.CharField(max_length=15, blank=True, default='', verbose_name='TELEFONE')
    estadocivil = models.CharField(
        max_length=20,
        choices=OPCOES_ESTADO_CIVIL,
        blank=True,
        default='',
        verbose_name='ESTADO CIVIL',
    )
    ocupacao_atual = models.CharField(max_length=100, blank=True, default='', verbose_name='OCUPAÇÃO ATUAL')
    cpf = models.CharField(
        max_length=14,
        blank=True,
        null=True,
        unique=True,
        db_index=True,
        verbose_name='CPF'
    )
    cnh = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        unique=True,
        verbose_name='CNH'
    )
    cnh_vencimento = models.DateField(blank=True, null=True, verbose_name='VENCIMENTO CNH')
    identidade = models.CharField(max_length=20, blank=True, default='', verbose_name='IDENTIDADE')
    orgao_expedidor = models.CharField(max_length=15, blank=True, default='', verbose_name='ÓRGÃO EXPEDIDOR')
    tipo_sangue = models.CharField(max_length=15, blank=True, default='', verbose_name='TIPO SANGUE')
    email = models.EmailField(blank=True, default='', verbose_name='EMAIL')
    escolaridade = models.CharField(max_length=50, blank=True, default='', verbose_name='ESCOLARIDADE')
    cursos = models.TextField(blank=True, default='', verbose_name='CURSOS')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-Hora cadastro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-Hora atualizado')

    class Meta:
        verbose_name = "GCM"
        verbose_name_plural = "GCMs"
        ordering = ['nome_guerra']

    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.nome.strip().upper()
        if self.nome_guerra:
            self.nome_guerra = self.nome_guerra.strip().upper()
        if self.matricula:
            self.matricula = self.matricula.replace('-', '').replace('.', '').strip().upper()

        if self.uf:
            self.uf = self.uf.strip().upper()

        # Garante que campos unique vazios sejam salvos como NULL (evita IntegrityError no Postgres)
        if self.cpf:
            self.cpf = self.cpf.replace('.', '').replace('-', '').strip()
        else:
            self.cpf = None

        if self.cnh:
            self.cnh = self.cnh.strip().upper()
        else:
            self.cnh = None

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_guerra} ({self.matricula})"
