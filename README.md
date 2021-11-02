# Projeto Cadastro


## Como rodar o projeto?
- Versão do python utilizado == 3.9
- Clone esse repositório.
- Crie um virtualenv com Python 3.
- Ative o virtualenv.
- Instale as dependências.
- Rode as migrações.
- Rodar o projeto

```
git clone https://github.com/jackteruya/Django-cadastro.git
cd django-cadastro
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py runserver
```

## O Projeto
- Após rodar o projeto, sera possível acessar através do http://127.0.0.1:8000/
- As APIs, endpoints:
  - http://127.0.0.1:8000/listar-mulheres-meeren/    # GET: retornando mulheres de meeren
  - http://127.0.0.1:8000/cadastro/<str:sexo>/       # GET: receber o sexo (m ou f) como parâmetro, filtrar e retornar a lista de pessoas, ordenanda por idade.
- A URL da tela para upload do arquivo .xlsx:
  - http://127.0.0.1:8000/dados-upload/              # POST: para fazer o upload do excel.
- Painel ADMIN:
  - http://127.0.0.1:8000/admin/

