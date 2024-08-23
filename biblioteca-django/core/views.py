from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from .models import Livro
from .serializers import LivroSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'POST'])
@csrf_exempt
def livro_list_create(request):    # /livros/
    if request.method == 'GET':
        # print('cheguei aqui')
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return JSONResponse(serializer.data)

    if request.method == 'POST':
        print('Entrou no POST')
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def livro_detail(request, pk):    # /livros/<int:pk>/
    livro = Livro.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return JSONResponse(serializer.data)

    if request.method == 'PUT':
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)