from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import SolicitacaoForm
from .models import Solicitacao

# Só a equipe do NAPNE (usuário com "Membro da equipe") vê o painel.
apenas_equipe = user_passes_test(lambda u: u.is_staff, login_url='login')


def index(request):
    return render(request, 'napne/index.html')


def criar_solicitacao(request):
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = SolicitacaoForm()
    return render(request, 'napne/criar_solicitacao.html', {'form': form})


def sucesso(request):
    return render(request, 'napne/sucesso.html')


@login_required
@apenas_equipe
def listar_solicitacoes(request):
    busca = request.GET.get('q', '').strip()
    solicitacoes = Solicitacao.objects.select_related('categoria')
    if busca:
        solicitacoes = solicitacoes.filter(
            Q(nome_completo__icontains=busca)
            | Q(matricula__icontains=busca)
            | Q(assunto__icontains=busca)
        )
    todas = Solicitacao.objects
    contexto = {
        'solicitacoes': solicitacoes,
        'busca': busca,
        'total': todas.count(),
        'pendentes': todas.filter(status='P').count(),
        'andamento': todas.filter(status='EA').count(),
        'concluidas': todas.filter(status='C').count(),
    }
    return render(request, 'napne/listar_solicitacoes.html', contexto)


@login_required
@apenas_equipe
@require_POST
def concluir_solicitacao(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    solicitacao.concluir()
    messages.success(request, f'Solicitação "{solicitacao.assunto}" marcada como concluída.')
    return redirect('painel')
