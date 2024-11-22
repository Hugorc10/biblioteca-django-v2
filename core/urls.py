from django.urls import path
from . import views

urlpatterns = [
    path('', views.APIRootView.as_view(), name='api-root'),
    path('user/', views.CreateUserAndGetToken.as_view(), name=views.CreateUserAndGetToken.name),
    path('livros/', views.BookList.as_view(), name=views.BookList.name),
    path('livros/<int:pk>/', views.BookDetail.as_view(), name=views.BookDetail.name),
    path('autores/', views.AuthorList.as_view(), name=views.AuthorList.name),
    path('autores/<int:pk>/', views.AuthorDetail.as_view(), name=views.AuthorDetail.name),
    path('categorias/', views.CategoryList.as_view(), name=views.CategoryList.name),
    path('categorias/<int:pk>/', views.CategoryDetail.as_view(), name=views.CategoryDetail.name),
    path('categorias/<int:pk>/livros/', views.BookListByCategory.as_view(), name=views.BookListByCategory.name),
    path('colecoes/', views.ColecaoListCreate.as_view(), name=views.ColecaoListCreate.name),
    path('colecoes/<int:pk>/', views.ColecaoDetail.as_view(), name=views.ColecaoDetail.name),
]