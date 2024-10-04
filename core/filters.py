from django_filters import rest_framework as filters
from .models import Book, Author, Category

class BooksFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains')
    autor = filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')
    categoria = filters.AllValuesFilter(field_name='categoria__nome')

    class Meta:
        model = Book
        fields = ['titulo', 'autor', 'categoria']

# Implement search filters for the name attribute, using the prefix ^ (starts with), for Category and Book
class CategoriesFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Category
        fields = ['nome']

class AuthorsFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Author
        fields = ['nome']