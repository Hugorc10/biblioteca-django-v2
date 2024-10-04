from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import generics
from core.filters import CategoriesFilter, BooksFilter, AuthorsFilter
from .models import Book, Category, Author
from .serializers import CategorySerializer, BookSerializer, AuthorSerializer

class APIRootView(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'categories.': reverse(CategoryList.name, request=request),
            'authors': reverse(AuthorList.name, request=request),
            'books': reverse(BookList.name, request=request),
        })

class BookList(generics.ListCreateAPIView):    # /livros/
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BooksFilter
    search_fields = ('^titulo',)
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']
    name = 'book-list'

class BookDetail(generics.RetrieveUpdateDestroyAPIView):    # /livros/<int:pk>/
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'

class CategoryList(generics.ListCreateAPIView):    # /categorias/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoriesFilter
    search_fields = ("^nome",)
    ordering_fields = ("nome",)
    name = 'category-list'

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):    # /categorias/<int:pk>/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'

class BookListByCategory(generics.ListAPIView):    # /categorias/<int:pk>/livros/
    serializer_class = BookSerializer
    name = 'book-list-by-category'

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Book.objects.filter(categoria=categoria)

class AuthorList(generics.ListCreateAPIView):    # /autores/
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorsFilter
    # ordering_fields = ['nome', 'birth_date']
    name = 'author-list'

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):    # /autores/<int:pk>/
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-detail'

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