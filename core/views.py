from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import status, generics
from core.filters import CategoriaFilter, LivroFilter, AutorFilter
from .models import Book, Category, Author
from .serializers import CategoriaSerializer, LivroSerializer, AutorSerializer

class APIRootView(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'categories.': reverse(CategoriesList.name, request=request),
            'author': reverse(AuthorsDetail.name, request=request),
            'books': reverse(BooksList.name, request=request),
        })

class BooksList(generics.ListCreateAPIView):    # /livros/
    queryset = Book.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    search_fields = ('^title',)
    ordering_fields = ['title', 'author', 'category', 'published_in']
    name = 'books-list'

class BooksDetail(generics.RetrieveUpdateDestroyAPIView):    # /livros/<int:pk>/
    queryset = Book.objects.all()
    serializer_class = LivroSerializer
    name = 'books-detail'

class CategoriesList(generics.ListCreateAPIView):    # /categorias/
    queryset = Category.objects.all()
    serializer_class = CategoriaSerializer
    filterset_class = CategoriaFilter
    search_fields = ("^name",)
    ordering_fields = ("name",)
    name = 'categories-list'

class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):    # /categorias/<int:pk>/
    queryset = Category.objects.all()
    serializer_class = CategoriaSerializer
    name = 'categories-detail'

class BooksListByCategory(generics.ListAPIView):    # /categorias/<int:pk>/livros/
    serializer_class = LivroSerializer
    name = 'books-list-by-category'

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Book.objects.filter(categoria=categoria)

class AuthorsList(generics.ListCreateAPIView):    # /autores/
    queryset = Author.objects.all()
    serializer_class = AutorSerializer
    filterset_class = AutorFilter
    ordering_fields = ['name']
    name = 'authors-list'

class AuthorsDetail(generics.RetrieveUpdateDestroyAPIView):    # /autores/<int:pk>/
    queryset = Author.objects.all()
    serializer_class = AutorSerializer
    name = 'authors-detail'

# class JSONResponse(HttpResponse):
# def __init__(self, data, **kwargs):
# content = JSONRenderer().render(data)
# kwargs['content_type'] = 'application/json'
# super(JSONResponse, self).__init__(content, **kwargs)

# @api_view(['GET', 'POST'])
# @csrf_exempt
# def livro_list_create(request):    # /livros/
#     if request.method == 'GET':
#         # print('cheguei aqui')
#         livros = Book.objects.all()
#         serializer = LivroSerializer(livros, many=True)
#         return JSONResponse(serializer.data)

#     if request.method == 'POST':
#         print('Entrou no POST')
#         serializer = LivroSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JSONResponse(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# @csrf_exempt
# def livro_detail(request, pk):    # /livros/<int:pk>/
#     livro = Book.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = LivroSerializer(livro)
#         return JSONResponse(serializer.data)

#     if request.method == 'PUT':
#         serializer = LivroSerializer(livro, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         livro.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)