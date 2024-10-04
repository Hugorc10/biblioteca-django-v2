from django.core.management.base import BaseCommand
from core.models import Category, Author, Book
class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):
        categoria_misterio = Category.objects.create(nome="Mistério")
        categoria_ficcao = Category.objects.create(nome="Ficção")
        categoria_fantasia = Category.objects.create(nome="Fantasia")
        categoria_romance = Category.objects.create(nome="Romance")
        autor_agatha_christie = Author.objects.create(nome="Agatha Christie")
        autor_arthur_c_clarke = Author.objects.create(nome="Arthur C. Clarke")
        autor_arthur_conan_doyle = Author.objects.create(nome="Arthur Conan Doyle")
        autor_cs_lewis = Author.objects.create(nome="C.S. Lewis")
        autor_emily_bronte = Author.objects.create(nome="Emily Brontë")
        autor_george_rr_martin = Author.objects.create(nome="George R.R. Martin")
        autor_isaac_asimov = Author.objects.create(nome="Isaac Asimov")
        autor_jrr_tolkien = Author.objects.create(nome="J.R.R. Tolkien")

        Book.objects.create(
            titulo="Assassinato no Expresso do Oriente",
            autor=autor_agatha_christie,
            categoria=categoria_misterio,
            publicado_em="1934-01-01",
        )
        Book.objects.create(
            titulo="Morte no Nilo",
            autor=autor_agatha_christie,
            categoria=categoria_misterio,
            publicado_em="1937-11-01",
        )
        Book.objects.create(
            titulo="2001: Uma Odisseia no Espaço",
            autor=autor_arthur_c_clarke,
            categoria=categoria_ficcao,
            publicado_em="1968-06-16",
        )
        Book.objects.create(
            titulo="Encontro com Rama",
            autor=autor_arthur_c_clarke,
            categoria=categoria_ficcao,
            publicado_em="1973-06-01",
        )
        Book.objects.create(
            titulo="O Cão dos Baskervilles",
            autor=autor_arthur_conan_doyle,
            categoria=categoria_misterio,
            publicado_em="1902-04-01",
        )
        Book.objects.create(
            titulo="Um Estudo em Vermelho",
            autor=autor_arthur_conan_doyle,
            categoria=categoria_misterio,
            publicado_em="1887-11-01",
        )
        Book.objects.create(
            titulo="As Crônicas de Nárnia",
            autor=autor_cs_lewis,
            categoria=categoria_fantasia,
            publicado_em="1950-10-16",
        )
        Book.objects.create(
            titulo="O Leão, a Feiticeira e o Guarda-Roupa",
            autor=autor_cs_lewis,
            categoria=categoria_fantasia,
            publicado_em="1950-10-16",
        )
        Book.objects.create(
            titulo="O Morro dos Ventos Uivantes",
            autor=autor_emily_bronte,
            categoria=categoria_romance,
            publicado_em="1847-12-01",
        )
        Book.objects.create(
            titulo="A Guerra dos Tronos",
            autor=autor_george_rr_martin,
            categoria=categoria_fantasia,
            publicado_em="1996-08-06",
        )
        Book.objects.create(
            titulo="A Fúria dos Reis",
            autor=autor_george_rr_martin,
            categoria=categoria_fantasia,
            publicado_em="1998-11-16",
        )
        Book.objects.create(
            titulo="Fundação",
            autor=autor_isaac_asimov,
            categoria=categoria_ficcao,
            publicado_em="1951-06-01",
        )
        Book.objects.create(
            titulo="Eu, Robô",
            autor=autor_isaac_asimov,
            categoria=categoria_ficcao,
            publicado_em="1950-12-02",
        )
        Book.objects.create(
            titulo="O Senhor dos Anéis",
            autor=autor_jrr_tolkien,
            categoria=categoria_fantasia,
            publicado_em="1954-07-29",
        )
        Book.objects.create(
            titulo="O Hobbit",
            autor=autor_jrr_tolkien,
            categoria=categoria_fantasia,
            publicado_em="1937-09-21",
        )