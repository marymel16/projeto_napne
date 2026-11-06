from django import forms
from django.conf import settings

from .models import Solicitacao


class SolicitacaoForm(forms.ModelForm):
    aceita_termos = forms.BooleanField(
        label="Autorizo o NAPNE a usar estes dados para entrar em contato e organizar meu atendimento.",
        error_messages={'required': 'Marque esta caixa para enviar o pedido.'},
    )

    class Meta:
        model = Solicitacao
        fields = [
            'nome_completo', 'matricula', 'email', 'telefone', 'curso', 'campus',
            'categoria', 'assunto', 'descricao', 'urgencia',
        ]
        labels = {
            'nome_completo': 'Nome completo',
            'matricula': 'Matrícula',
            'email': 'E-mail institucional',
            'telefone': 'Telefone ou WhatsApp (opcional)',
            'curso': 'Curso',
            'campus': 'Campus',
            'categoria': 'Tipo de necessidade',
            'assunto': 'Assunto',
            'descricao': 'Conte o que você precisa',
            'urgencia': 'Urgência',
        }
        widgets = {'descricao': forms.Textarea(attrs={'rows': 5})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "Selecione uma opção"
        for nome, campo in self.fields.items():
            if isinstance(campo.widget, forms.CheckboxInput):
                campo.widget.attrs['class'] = 'form-check-input'
            elif isinstance(campo.widget, forms.Select):
                campo.widget.attrs['class'] = 'form-select'
            else:
                campo.widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        dominios = getattr(settings, 'EMAIL_DOMINIOS_PERMITIDOS', [])
        if dominios:
            dominio = email.rsplit('@', 1)[-1]
            if not any(dominio == d or dominio.endswith('.' + d) for d in dominios):
                raise forms.ValidationError(
                    "Use seu e-mail institucional (terminado em ifrn.edu.br)."
                )
        return email
