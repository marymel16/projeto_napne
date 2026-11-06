from django.core.validators import RegexValidator
from django.db import models


class Categoria(models.Model):
    """Tipo de necessidade/atendimento (equivale à Categoria do slide)."""
    nome = models.CharField(max_length=60, unique=True)
    descricao = models.TextField(blank=True, null=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Solicitacao(models.Model):
    """Pedido de atendimento enviado por um aluno (equivale à Tarefa do slide)."""
    URGENCIAS = [
        ("B", "Baixa"),
        ("M", "Média"),
        ("A", "Alta"),
    ]
    STATUS = [
        ("P", "Pendente"),
        ("EA", "Em andamento"),
        ("C", "Concluída"),
    ]

    nome_completo = models.CharField(max_length=120)
    matricula = models.CharField(
        max_length=16,
        validators=[RegexValidator(r'^\d{6,16}$', 'Use só números (de 6 a 16 dígitos).')],
    )
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    curso = models.CharField(max_length=100)
    campus = models.CharField(max_length=80)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="solicitacoes",
    )
    assunto = models.CharField(max_length=100)
    descricao = models.TextField()
    urgencia = models.CharField(max_length=2, choices=URGENCIAS, default="M")
    status = models.CharField(max_length=2, choices=STATUS, default="P")
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criada_em']
        verbose_name = 'solicitação'
        verbose_name_plural = 'solicitações'

    def concluir(self):
        self.status = "C"
        self.save(update_fields=["status"])

    def __str__(self):
        return f"{self.assunto} - {self.nome_completo}"
