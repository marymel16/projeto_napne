from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('solicitar/', views.criar_solicitacao, name='criar_solicitacao'),
    path('solicitacao-enviada/', views.sucesso, name='sucesso'),
    path('painel/', views.listar_solicitacoes, name='painel'),
    path('painel/<int:pk>/concluir/', views.concluir_solicitacao, name='concluir_solicitacao'),
]
