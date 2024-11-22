from rest_framework import serializers
from .models import Category, Author, Book, Colecao
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)
    token = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'token']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.save()
        return instance

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.save()
        return instance

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(max_length=100)

     # Para envio dos dados (criação e atualização)
    autor = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    publicado_em = serializers.DateField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.autor = validated_data.get('autor', instance.autor)
        instance.categoria = validated_data.get('categoria', instance.categoria)
        instance.publicado_em = validated_data.get('publicado_em', instance.publicado_em)
        instance.save()
        return instance

class ColecaoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=100)
    descricao = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    livros = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), many=True)
    colecionador = serializers.StringRelatedField()

    def create(self, validated_data):
        request = self.context.get('request')  # Get the request from serializer context
        colecionador = request.user if request else None  # Assign authenticated user

        livros_data = validated_data.pop('livros', [])
        colecao = Colecao.objects.create(colecionador=colecionador, **validated_data)
        colecao.livros.set(livros_data)
        return colecao

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        # Update ManyToMany relationships

        livros_data = validated_data.get('livros', [])
        if livros_data:
            instance.livros.set(livros_data)

        instance.save()
        return instance