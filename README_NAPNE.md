# Sistema Web de Apoio ao NAPNE

## 1. Descrição

O **Sistema Web de Apoio ao NAPNE** é uma aplicação web desenvolvida como projeto acadêmico com Django. Seu objetivo é facilitar o envio e o gerenciamento de solicitações de atendimento ao Núcleo de Apoio às Pessoas com Necessidades Específicas (NAPNE).

A aplicação permite que estudantes do IFRN preencham um formulário para solicitar apoio. A equipe do NAPNE, por meio de uma área restrita, pode consultar as solicitações recebidas, pesquisar registros e acompanhar seus status.

O sistema busca organizar o primeiro contato entre os estudantes e o setor, reunindo as solicitações em um ambiente próprio. Ele não substitui o SUAP nem realiza, por si só, o acompanhamento pedagógico completo dos estudantes.

## 2. Objetivos

- Disponibilizar um formulário on-line para solicitação de atendimento ao NAPNE.
- Reunir as solicitações enviadas pelos estudantes em um painel de consulta.
- Facilitar a localização de solicitações por nome, matrícula ou assunto.
- Permitir que a equipe acompanhe o andamento dos pedidos.
- Organizar as solicitações por categoria, urgência e situação.

## 3. Funcionalidades

As funcionalidades descritas nesta seção foram identificadas no código do projeto incluído neste repositório.

### 3.1. Área pública

- **Página inicial:** apresenta informações sobre o serviço e orienta o estudante sobre como solicitar atendimento.
- **Formulário de solicitação:** permite informar nome completo, matrícula, e-mail institucional, telefone (opcional), curso, campus, categoria, assunto, descrição e urgência.
- **Validação de dados:** verifica os campos obrigatórios, valida o formato da matrícula e, por padrão, aceita e-mails do domínio `ifrn.edu.br`.
- **Consentimento:** exige que o estudante marque a autorização para que os dados sejam utilizados no contato e na organização do atendimento.
- **Confirmação de envio:** após o envio válido, apresenta uma página de confirmação.

### 3.2. Área restrita da equipe

- **Login:** permite a autenticação dos integrantes autorizados da equipe.
- **Painel de solicitações:** apresenta a lista de pedidos recebidos.
- **Indicadores:** mostra o total de solicitações e as quantidades pendentes, em andamento e concluídas.
- **Busca:** permite pesquisar solicitações por nome do estudante, matrícula ou assunto.
- **Conclusão de solicitação:** permite marcar um pedido como concluído.
- **Administração:** o Django Admin permite gerenciar categorias e consultar ou editar solicitações, conforme as permissões da conta.

### 3.3. Situação das funcionalidades

O formulário, a confirmação de envio, a autenticação da equipe, o painel com busca e indicadores e a ação de concluir solicitações estão implementados no código. Recursos como consulta de grade curricular, localização de horários e professores e leitura de conteúdo em áudio **não fazem parte da versão atual**.

## 4. Tecnologias utilizadas

- **Python:** linguagem de programação do projeto.
- **Django 6.1.3:** framework utilizado para desenvolver a aplicação web, gerenciar rotas, formulários, autenticação e acesso ao banco de dados.
- **SQLite:** banco de dados configurado para o ambiente de desenvolvimento.
- **HTML:** estrutura das páginas.
- **CSS:** estilos personalizados da aplicação.
- **Bootstrap 5.3.3:** biblioteca utilizada para componentes e organização visual da interface.
- **Bootstrap Icons 1.11.3:** ícones da interface.
- **Git e GitHub:** controle de versão e hospedagem do repositório, quando utilizados pela equipe.

A interface também carrega a fonte Atkinson Hyperlegible por meio do Google Fonts.

## 5. Pré-requisitos

Para executar o projeto localmente, é necessário:

- Python em versão compatível com o Django especificado no arquivo `requirements.txt`.
- pip, para instalação das dependências.
- Git, caso o repositório seja clonado pelo terminal.
- Navegador web atualizado.

As dependências Python estão listadas em `requirements.txt`.

## 6. Instalação e execução

Os comandos abaixo consideram o Windows com PowerShell. Execute-os no terminal, dentro da pasta que contém o arquivo `manage.py`.

### 6.1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd PASTA_DO_PROJETO
```

Substitua `URL_DO_REPOSITORIO` pelo endereço do repositório e `PASTA_DO_PROJETO` pelo nome da pasta criada.

Se o projeto já estiver baixado, basta abrir no terminal a pasta em que está o `manage.py`.

### 6.2. Criar o ambiente virtual

```powershell
python -m venv venv
```

### 6.3. Ativar o ambiente virtual

```powershell
.env\Scripts\Activate
```

No Linux ou macOS, utilize:

```bash
source venv/bin/activate
```

### 6.4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6.5. Aplicar as migrações do banco de dados

```bash
python manage.py migrate
```

### 6.6. Criar uma conta administrativa para a equipe

```bash
python manage.py createsuperuser
```

Siga as instruções do terminal para definir usuário e senha. Para acessar o painel interno da equipe, a conta precisa ter permissão de equipe (`is_staff`). A conta criada pelo comando `createsuperuser` normalmente já possui essa permissão.

### 6.7. Iniciar o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse no navegador:

- Página inicial: http://127.0.0.1:8000/
- Formulário de solicitação: http://127.0.0.1:8000/solicitar/
- Login da equipe: http://127.0.0.1:8000/usuarios/login/
- Painel da equipe: http://127.0.0.1:8000/painel/
- Administração do Django: http://127.0.0.1:8000/admin/

O painel exige autenticação e permissão de equipe. Para encerrar o servidor, pressione `Ctrl + C` no terminal.

**Observação:** `runserver` é destinado ao desenvolvimento e a testes locais, não à publicação em produção.

## 7. Estrutura do projeto

A estrutura principal do repositório é:

```text
projeto_napne/
├── manage.py
├── requirements.txt
├── setup/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── napne/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── usuarios/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/
│   ├── base.html
│   ├── napne/
│   └── usuarios/
└── static/
    ├── css/
    └── img/
```

- `manage.py`: executa comandos administrativos do Django.
- `setup/`: contém as configurações gerais e as rotas principais do projeto.
- `napne/`: contém os modelos, formulários, regras e páginas relacionadas às solicitações.
- `usuarios/`: contém as rotas de autenticação da equipe.
- `templates/`: reúne os modelos HTML das páginas.
- `static/`: armazena arquivos estáticos, como CSS e imagens.
- `requirements.txt`: registra as dependências Python.

## 8. Equipe

Integrantes responsáveis pelo desenvolvimento:

- **[Maria Heloisa Pinheiro de Souza]**
- **[Mary Mel Rebouças Marcelino]**


## 9. Segurança e observações

As solicitações contêm dados pessoais dos estudantes. Por isso, o acesso ao painel deve permanecer restrito a pessoas autorizadas, e os dados não devem ser compartilhados publicamente.

A versão do repositório está configurada para desenvolvimento local. Antes de qualquer publicação em ambiente real, é necessário revisar as configurações de segurança do Django, incluindo a chave secreta, o modo `DEBUG`, os hosts permitidos, a proteção do banco de dados e os procedimentos de implantação. O uso em contexto institucional também deve observar a legislação aplicável à proteção de dados pessoais.

## 10. Estado atual do projeto

A versão analisada já possui o fluxo de envio de solicitações pelos estudantes e o painel restrito para consulta e atualização do status dos pedidos. A aplicação está estruturada com Django e utiliza SQLite como banco de dados padrão.

Funcionalidades adicionais poderão ser incorporadas em versões futuras, de acordo com as necessidades identificadas junto ao NAPNE.
