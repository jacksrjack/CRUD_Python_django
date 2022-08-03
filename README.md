# CRUD com Python

O aplicativo a seguir realiza o crud na linguagem Python. Você poderá optar por utilizar o banco SQLite ou Mysql.

## Instalação

  1. Através do CMD, acesse a pasta do projeto e execute o comando `$ pip install virtualenv`
  2. `$ python -m venv venv`
  3. `$ venv\scripts\activate`
  4. `$ pip install -r requirements.txt`
  5. `$ python manage.py makemigrations`
  6. `$ python manage.py migrate`
  7. `$ python manage.py runserver`

  
## Funcionalidades Implementadas

  1. Cadastrar uma série
  2. Listar as séries cadastradas com paginação
  3. Editar dados de uma série
  4. Ver e deletar uma série
  
## Bibliotecas
  + `django`
  +  `mysql`

## Observações
  + Para utilizar o banco SQLite, basta executar as instalações normalmente.
  + Para utilizar o banco MySQL, você devera alterar as configurações do arquivo `settings.py`. Para isso, basta comentar as linhas `80` e `81` e remover os comentários das linhas `82 até 87`, inserindo também os dados equivalente ao seu banco de dados.