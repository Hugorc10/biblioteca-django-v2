from django_filters import rest_framework as filters
from .models import Book, Author, Category

class LivroFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(field_name='autor__nome')
    category = filters.CharFilter(field_name='categoria__nome')

    class Meta:
        model = Book
        fields = ['title', 'author', 'category']

# Implement search filters for the name attribute, using the prefix ^ (starts with), for Category and Book
class CategoriaFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Category
        fields = ['name']

class AutorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Author
        fields = ['name']