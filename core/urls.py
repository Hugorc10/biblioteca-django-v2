from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.APIRootView.as_view(), name='api-root'),
    path('books/', views.BooksList.as_view(), name=views.BooksList.name),
    path('books/<int:pk>/', views.BooksDetail.as_view(), name=views.BooksDetail.name),
    path('authors/', views.AuthorsList.as_view(), name=views.AuthorsList.name),
    path('authors/<int:pk>/', views.AuthorsDetail.as_view(), name=views.AuthorsDetail.name),
    path('categories/', views.CategoriesList.as_view(), name=views.CategoriesList.name),
    path('categories/<int:pk>/', views.CategoriesDetail.as_view(), name=views.CategoriesDetail.name),
    path('categories/<int:pk>/books/', views.BooksListByCategory.as_view(), name=views.BooksListByCategory.name),

]