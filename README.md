# Biblioteca Django

## Descrição

Esta é uma API RESTful para gerenciar uma coleção de livros, desenvolvida com Django e Django REST Framework. A API permite criar, visualizar, atualizar e excluir livros da coleção.

## Funcionalidades

- **Listar livros:** Retorna uma lista de todos os livros cadastrados.
- **Retona livro especifico:** Retorna os detalhes de um livro específico.
- **Criar livro:** Adiciona um novo livro à coleção.
- **Atualizar livro:** Atualiza as informações de um livro existente.
- **Excluir livro:** Remove um livro da coleção.

## Tecnologias

- [Django](https://www.djangoproject.com/) - Framework web utilizado para o desenvolvimento.
- [Django REST Framework](https://www.django-rest-framework.org/) - Biblioteca para construção de APIs RESTful em Django.
- [SQLite](https://www.sqlite.org/index.html) - Banco de dados padrão para desenvolvimento.

## Requisitos

- Python 3.8+
- Django 5.x
- Django REST Framework 3.x

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone git@github.com:Hugorc10/biblioteca-django.git
   cd biblioteca-django

2. **Crie o ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt

4. **Configure o banco de dados:**

   ```bash
   python manage.py makemigrations core
   python manage.py migrate

5. **Se o banco de dados SQLite estiver vazio, popule com esse comando:

   ```bash
   python manage.py populate_db

6. **Inicia o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

   A API estará disponível em http://127.0.0.1:8000/.
