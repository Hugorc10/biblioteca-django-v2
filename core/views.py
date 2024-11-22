from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from core.filters import CategoriesFilter, BooksFilter, AuthorsFilter
from .models import Book, Category, Author, Colecao
from .serializers import CategorySerializer, BookSerializer, AuthorSerializer, ColecaoSerializer, UserSerializer
from .custom_permissions import CustomPermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

class APIRootView(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(CreateUserAndGetToken.name, request=request),
            'categories.': reverse(CategoryList.name, request=request),
            'authors': reverse(AuthorList.name, request=request),
            'books': reverse(BookList.name, request=request),
            'colecao': reverse(ColecaoListCreate.name, request=request)
        })

class CreateUserAndGetToken(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new user
            user = serializer.save()

            # Generate or retrieve the token for the user
            token, created = Token.objects.get_or_create(user=user)

            # Return the token in the response
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)

        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    name = 'create-user-and-get-token'


class BookList(generics.ListCreateAPIView):    # /livros/
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BooksFilter
    permission_classes = (permissions.AllowAny,)
    search_fields = ('^titulo',)
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']
    name = 'book-list'

class BookDetail(generics.RetrieveUpdateDestroyAPIView):    # /livros/<int:pk>/
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.AllowAny,)
    name = 'book-detail'

class CategoryList(generics.ListCreateAPIView):    # /categorias/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoriesFilter
    permission_classes = (permissions.AllowAny,)
    search_fields = ("^nome",)
    ordering_fields = ("nome",)
    name = 'category-list'

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):    # /categorias/<int:pk>/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)
    name = 'category-detail'

class BookListByCategory(generics.ListAPIView):    # /categorias/<int:pk>/livros/
    serializer_class = BookSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Book.objects.filter(categoria=categoria)

    name = 'book-list-by-category'

class AuthorList(generics.ListCreateAPIView):    # /autores/
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorsFilter
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)
    # ordering_fields = ['nome', 'birth_date']
    name = 'author-list'

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):    # /autores/<int:pk>/
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)
    name = 'author-detail'

class ColecaoListCreate(generics.ListCreateAPIView):    # /colecoes/
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    name = 'colecao-list-create'

class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):    # /colecoes/<int:pk>/
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        CustomPermission,
    )
    name = 'colecao-detail'

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