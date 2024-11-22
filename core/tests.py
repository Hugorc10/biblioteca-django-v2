import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
# from rest_framework.test import APITestCase
from .models import Category, Author, Book, Colecao
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(username="user1", password="password1")

@pytest.fixture
def author(db):
    return Author.objects.create(nome="Autor de teste")

@pytest.fixture
def book(db, author):
    return Book.objects.create(
        titulo="Test Book",
        autor=author,
        categoria=Category.objects.create(nome="Ficção"),
        publicado_em="2023-10-08",
    )

@pytest.fixture
def colecao(user):
    # return Colecao.objects.create(nome="Minha Coleção", colecionador=user)
    return Colecao.objects.create(
        nome="Coleção 1", descricao="Descrição da Coleção 1", colecionador=user
    )

def test_collection_creation(api_client, user, book):
    api_client.force_authenticate(user=user)
    url = reverse("colecao-list-create")
    data = {
        "nome": "Nova Coleção",
        "descricao": "Descrição da coleção",
        "livros": [book.id],
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["nome"] == "Nova Coleção"
    assert response.data["colecionador"] == user.username

def test_permission_edition_collection(api_client, user, colecao, book):
    api_client.force_authenticate(user=user)
    url = reverse("colecao-detail", args=[colecao.id])
    data = {"nome": "Coleção Atualizada", "descricao": "Descrição atualizada",
            "livros": [book.id], "colecionador": [user.id]}
    response = api_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["nome"] == "Coleção Atualizada"

def test_permission_unauthenticated_user(api_client, colecao):
    url = reverse("colecao-detail", args=[colecao.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_listing_collections(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("colecao-list-create")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0