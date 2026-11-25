from django.db import models


class Veiculo(models.Model):
    OPCOES_CATEGORIA = [
        ('AUTOMOVEL', 'Automóvel'),
        ('MOTOCICLETA', 'Motocicleta'),
        ('MOTO_ELETRICA_1000W', 'Moto elétrica até 1000W'),
        ('CAMINHONETE', 'Caminhonete'),
        ('CAMINHAO', 'Caminhão'),
        ('ONIBUS', 'Ônibus'),
        ('MICRO_ONIBUS', 'Micro-Ônibus'),
        ('REBOQUE', 'Reboque'),
        ('BICICLETA', 'Bicicleta'),
        ('OUTRO', 'Outro'),
    ]

    categoria = models.CharField(
        max_length=30,
        choices=OPCOES_CATEGORIA,
        default='AUTOMOVEL',
        verbose_name='CATEGORIA'
    )
    placa = models.CharField(
        max_length=8,
        blank=True,
        default='',
        db_index=True,
        verbose_name='PLACA'
    )
    uf = models.CharField(max_length=2, blank=True, default='', verbose_name='UF')
    marca_modelo = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name='MARCA / MODELO'
    )
    cor = models.CharField(max_length=20, blank=True, default='', verbose_name='COR')
    ano_fabricacao = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        verbose_name='ANO FABRICAÇÃO'
    )
    ano_modelo = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        verbose_name='ANO MODELO'
    )
    chassi = models.CharField(
        max_length=17,
        blank=True,
        default='',
        db_index=True,
        verbose_name='CHASSI'
    )
    numero_motor = models.CharField(
        max_length=30,
        blank=True,
        default='',
        verbose_name='NÚMERO DO MOTOR'
    )
    situacao_veiculo = models.CharField(
        max_length=50,
        blank=True,
        default='',
        verbose_name='SITUAÇÃO DO VEÍCULO'
    )
    avarias = models.CharField(max_length=150, blank=True, default='', verbose_name='AVARIAS')
    observacoes = models.TextField(blank=True, default='', verbose_name='OBSERVAÇÕES')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-Hora cadastro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-Hora atualizado')

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        ordering = ['placa', 'marca_modelo']

    def save(self, *args, **kwargs):
        if self.placa:
            self.placa = self.placa.replace('-', '').replace(' ', '').strip().upper()
        if self.uf:
            self.uf = self.uf.strip().upper()
        if self.marca_modelo:
            self.marca_modelo = self.marca_modelo.strip().upper()
        if self.cor:
            self.cor = self.cor.strip().upper()
        if self.chassi:
            self.chassi = self.chassi.replace(' ', '').strip().upper()
        if self.numero_motor:
            self.numero_motor = self.numero_motor.replace(' ', '').strip().upper()
        if self.situacao_veiculo:
            self.situacao_veiculo = self.situacao_veiculo.strip().upper()
        if self.avarias:
            self.avarias = self.avarias.strip().upper()
        if self.observacoes:
            self.observacoes = self.observacoes.strip().upper()

        super().save(*args, **kwargs)

    def __str__(self):
        identificador = self.placa if self.placa else (self.chassi or self.numero_motor or 'SEM IDENTIFICAÇÃO')
        return f"{self.marca_modelo} - {identificador}" if self.marca_modelo else identificador


class Envolvido(models.Model):
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

    nome = models.CharField(max_length=150, db_index=True, verbose_name='NOME')
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
        default='SOLTEIRO',
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
    identidade = models.CharField(max_length=20, blank=True, default='', verbose_name='IDENTIDADE')
    orgao_expedidor = models.CharField(max_length=15, blank=True, default='', verbose_name='ÓRGÃO EXPEDIDOR')
    email = models.EmailField(blank=True, default='', verbose_name='EMAIL')
    escolaridade = models.CharField(max_length=50, blank=True, default='', verbose_name='ESCOLARIDADE')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-Hora cadastro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-Hora atualizado')

    class Meta:
        verbose_name = 'Envolvido'
        verbose_name_plural = 'Envolvidos'
        ordering = ['nome']

    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.nome.strip().upper()
        if self.pai:
            self.pai = self.pai.strip().upper()
        if self.mae:
            self.mae = self.mae.strip().upper()
        if self.uf:
            self.uf = self.uf.strip().upper()

        if self.cpf:
            self.cpf = self.cpf.replace('.', '').replace('-', '').strip()
        else:
            self.cpf = None

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} ({self.cpf})" if self.cpf else self.nome


class Boletim(models.Model):
    OPCOES_STATUS = [
        ('EM_ANDAMENTO', 'Em Andamento'),
        ('FINALIZADA', 'Finalizada'),
    ]
    OPCOES_ACIONAMENTO = [
        ('CENTRAL_COMUNICACOES', 'Central de comunicações'),
        ('DIRETAMENTE_GUARDA', 'Diretamente ao Guarda'),
        ('DENUNCIA_ANONIMA', 'Denúncia anônima'),
        ('DEPARANDO_FATO', 'Deparando com o fato'),
        ('INICIATIVA', 'Iniciativa'),
    ]
    OPCOES_BOLETIM = [
        ('BOLETIM_OCORRENCIA', 'Boletim de Ocorrência'),
        ('BOLETIM_INTERVENCAO', 'Boletim de Intervenção'),
    ]

    tipo_boletim = models.CharField(
        max_length=30,
        choices=OPCOES_BOLETIM,
        default='BOLETIM_INTERVENCAO',
        verbose_name='TIPO DE BOLETIM'
    )
    status = models.CharField(
        max_length=30,
        choices=OPCOES_STATUS,
        default='EM_ANDAMENTO',
        db_index=True,
        verbose_name='STATUS'
    )
    numero_boletim = models.CharField(
        max_length=15,
        unique=True,
        db_index=True,
        verbose_name='Boletim Nº'
    )
    numero_folha = models.CharField(max_length=6, blank=True, default='', verbose_name='FOLHA Nº')

    destinatario = models.CharField(max_length=255, blank=True, default='', verbose_name='DESTINATÁRIO')
    data_emissao = models.DateField(blank=True, null=True, verbose_name='DATA EMISSÃO')
    numero_reds = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        unique=True,
        db_index=True,
        verbose_name='NÚMERO REDS'
    )

    tipificacao_ocorrencia = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name='TIPIFICAÇÃO DA OCORRÊNCIA'
    )

    # ----- DO FATO -------------------------------------------------------------------------
    acionamento = models.CharField(
        max_length=30,
        choices=OPCOES_ACIONAMENTO,
        default='CENTRAL_COMUNICACOES',
        verbose_name='ACIONAMENTO'
    )
    data_hora_inicio = models.DateTimeField(blank=True, null=True, db_index=True, verbose_name='DATA-HORA INÍCIO')
    data_hora_acionamento = models.DateTimeField(blank=True, null=True, verbose_name='DATA-HORA ACIONAMENTO')
    data_hora_final = models.DateTimeField(blank=True, null=True, verbose_name='DATA-HORA FINAL')

    descricao_natureza = models.CharField(max_length=150, blank=True, default='', verbose_name='DESCRIÇÃO NATUREZA')
    orgao = models.CharField(max_length=100, blank=True, default='', verbose_name='ÓRGÃO')
    setor = models.CharField(max_length=100, blank=True, default='', verbose_name='SETOR')

    endereco_dofato = models.CharField(max_length=255, blank=True, default='', verbose_name='ENDEREÇO')
    numero_dofato = models.CharField(max_length=20, blank=True, default='', verbose_name='NÚMERO')
    complemento = models.CharField(max_length=100, blank=True, default='', verbose_name='COMPLEMENTO')
    bairro_dofato = models.CharField(max_length=100, blank=True, default='', verbose_name='BAIRRO')
    cidade_dofato = models.CharField(max_length=100, blank=True, default='', verbose_name='CIDADE')
    uf_dofato = models.CharField(max_length=2, blank=True, default='', verbose_name='UF')

    # ----- HISTÓRICO -----------------------------------------------------------------------
    historico = models.TextField(blank=True, default='', verbose_name='HISTÓRICO')

    # ----- RELATOR E GUARNIÇÃO -------------------------------------------------------------
    relatorgcm = models.ForeignKey(
        'gcms.Gcm',
        on_delete=models.PROTECT,
        related_name='boletins_relatados',
        verbose_name='RELATOR',
        blank=True,
        null=True
    )
    relator_ocupacao_atual = models.CharField(max_length=50, blank=True, default='', verbose_name='CARGO DO RELATOR')
    relator_documento = models.CharField(max_length=50, blank=True, default='', verbose_name='DOCUMENTO DO RELATOR')

    coordenar_turno = models.ForeignKey(
        'gcms.Gcm',
        on_delete=models.PROTECT,
        related_name='boletins_coordenados',
        verbose_name='COORDENADOR DO TURNO',
        blank=True,
        null=True
    )
    guarnicao = models.ManyToManyField(
        'gcms.Gcm',
        related_name='boletins_guarnicao',
        blank=True,
        verbose_name='GUARNIÇÃO / APOIO'
    )

    # ----- AUTORIDADE ----------------------------------------------------------------------
    autoridadenome = models.CharField(max_length=255, blank=True, default='', verbose_name='AUTORIDADE')
    autoridadedocumento = models.CharField(max_length=50, blank=True, default='', verbose_name='DOCUMENTO DA AUTORIDADE')
    data_recebimento_autoridade = models.DateField(blank=True, null=True, verbose_name='DATA RECEBIMENTO')

    # ----- RELACIONAMENTOS MANY-TO-MANY EXPLÍCITOS -----------------------------------------
    envolvidos = models.ManyToManyField(
        Envolvido,
        through='BoletimEnvolvimento',
        related_name='boletins_envolvido',
        verbose_name='ENVOLVIDOS'
    )
    veiculos = models.ManyToManyField(
        Veiculo,
        through='BoletimVeiculo',
        related_name='boletins_veiculo',
        verbose_name='VEÍCULOS'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-Hora cadastro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-Hora atualizado')

    class Meta:
        verbose_name = 'Boletim'
        verbose_name_plural = 'Boletins'
        ordering = ['-data_hora_inicio', '-created_at']

    def save(self, *args, **kwargs):
        if self.numero_boletim:
            self.numero_boletim = self.numero_boletim.strip().upper()
        if self.uf_dofato:
            self.uf_dofato = self.uf_dofato.strip().upper()

        # Evita IntegrityError no Postgres quando numero_reds ficar vazio
        if self.numero_reds:
            self.numero_reds = self.numero_reds.strip().upper()
        else:
            self.numero_reds = None

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_tipo_boletim_display()} Nº {self.numero_boletim}"


class BoletimEnvolvimento(models.Model):
    TIPOS_ENVOLVIMENTO = [
        ('SOLICITANTE', 'Solicitante'),
        ('VITIMA', 'Vítima'),
        ('AUTOR', 'Autor'),
        ('TESTEMUNHA', 'Testemunha'),
        ('SOCORRIDO', 'Socorrido/Vítima'),
        ('CONDUTOR', 'Condutor'),
        ('OUTRO', 'Outro'),
    ]

    boletim = models.ForeignKey(
        Boletim,
        on_delete=models.CASCADE,
        related_name='envolvimentos',
        verbose_name='BOLETIM'
    )
    envolvido = models.ForeignKey(
        Envolvido,
        on_delete=models.CASCADE,
        related_name='participacoes',
        verbose_name='ENVOLVIDO'
    )

    tipo_envolvimento = models.CharField(
        max_length=30,
        choices=TIPOS_ENVOLVIMENTO,
        verbose_name='TIPO DE ENVOLVIMENTO'
    )
    conduzido_delegacia = models.BooleanField(default=False, verbose_name='CONDUZIDO À DELEGACIA')
    resistencia_abordagem = models.BooleanField(default=False, verbose_name='RESISTÊNCIA À ABORDAGEM')
    uso_algemas = models.BooleanField(default=False, verbose_name='USO DE ALGEMAS')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-Hora cadastro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-Hora atualizado')

    class Meta:
        verbose_name = 'Envolvimento no Boletim'
        verbose_name_plural = 'Envolvimentos no Boletim'
        constraints = [
            models.UniqueConstraint(fields=['boletim', 'envolvido'], name='unique_boletim_envolvido')
        ]

    def __str__(self):
        return f"{self.envolvido.nome} - {self.get_tipo_envolvimento_display()} no Boletim {self.boletim.numero_boletim}"


class BoletimVeiculo(models.Model):
    OPCOES_PROCEDIMENTO = [
        ('APREENDIDO', 'Apreendido'),
        ('RETIDO', 'Retido'),
        ('REMOVIDO', 'Removido'),
        ('LIBERADO_LOCAL', 'Liberado no Local'),
        ('APENAS_ENVOLVIDO', 'Apenas envolvido'),
    ]

    boletim = models.ForeignKey(
        Boletim,
        on_delete=models.CASCADE,
        related_name='veiculos_associados',
        verbose_name='BOLETIM'
    )
    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.CASCADE,
        related_name='historico_boletins',
        verbose_name='VEÍCULO'
    )
    procedimento_adotado = models.CharField(
        max_length=30,
        choices=OPCOES_PROCEDIMENTO,
        default='APENAS_ENVOLVIDO',
        verbose_name='PROCEDIMENTO ADOTADO'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-Hora cadastro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-Hora atualizado')

    class Meta:
        verbose_name = 'Veículo no Boletim'
        verbose_name_plural = 'Veículos no Boletim'
        constraints = [
            models.UniqueConstraint(fields=['boletim', 'veiculo'], name='unique_boletim_veiculo')
        ]

    def __str__(self):
        return f"{self.veiculo} - {self.get_procedimento_adotado_display()} no Boletim {self.boletim.numero_boletim}"
