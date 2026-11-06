from django.db import migrations

CATEGORIAS = [
    ("Deficiência física ou mobilidade reduzida", "Acessibilidade de espaços, mobiliário, deslocamento e tecnologias de apoio."),
    ("Deficiência visual (cegueira ou baixa visão)", "Materiais ampliados ou em formato acessível, leitores de tela, orientação."),
    ("Deficiência auditiva ou surdez", "Intérprete de Libras, legendas, materiais visuais."),
    ("Deficiência intelectual", "Adaptações pedagógicas e acompanhamento."),
    ("Transtorno do Espectro Autista (TEA)", "Apoio pedagógico, rotina e adaptações do ambiente."),
    ("Transtornos de aprendizagem ou TDAH", "Estratégias de estudo e adaptações de avaliação."),
    ("Altas habilidades ou superdotação", "Enriquecimento curricular e acompanhamento."),
    ("Outro ou ainda não sei informar", "A equipe do NAPNE ajuda a entender o melhor atendimento."),
]


def criar(apps, schema_editor):
    Categoria = apps.get_model('napne', 'Categoria')
    for nome, descricao in CATEGORIAS:
        Categoria.objects.get_or_create(nome=nome, defaults={'descricao': descricao})


def remover(apps, schema_editor):
    Categoria = apps.get_model('napne', 'Categoria')
    Categoria.objects.filter(nome__in=[n for n, _ in CATEGORIAS], solicitacoes__isnull=True).delete()


class Migration(migrations.Migration):
    dependencies = [('napne', '0001_initial')]
    operations = [migrations.RunPython(criar, remover)]
