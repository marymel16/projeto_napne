# Projeto NAPNE (Django)

Formulário para estudantes do IFRN pedirem atendimento ao NAPNE + painel para a equipe.

## Rodar (VS Code, terminal na pasta do projeto)
1. python -m venv venv
2. Ativar: Windows `venv\Scripts\activate` | Mac/Linux `source venv/bin/activate`
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

Páginas: / (início) · /solicitar/ (formulário) · /painel/ (equipe) · /admin/
