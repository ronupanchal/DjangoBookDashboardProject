from django.urls import path
from . import views
app_name = 'academy'

urlpatterns =[
    path('', views.index, name='index'),
    path('genre/create/', views.GenreView.as_view(), name='genre_create'),
    path('genre/list/', views.GenreList.as_view(), name='genre_list'),
    path('genre/update/<int:pk>', views.GenreUpdateView.as_view(), name='genre_update'),
    path('genre/delete/<int:pk>', views.GenreDeleteView.as_view(), name='genre_delete'),
    #------------
    path('language/create/', views.LanguageView.as_view(), name='language_create'),
    path('language/list/', views.LanguageList.as_view(), name='language_list'),
    path('language/update/<int:pk>', views.LanguageUpdateView.as_view(), name='language_update'),
    path('language/delete/<int:pk>', views.LanguageDeleteView.as_view(), name='language_delete'),
    #---------
    path('author/create/', views.AuthorView.as_view(), name='author_create'),
    path('author/list/', views.AuthorList.as_view(), name='author_list'),
    path('author/update/<int:pk>', views.AuthorUpdateView.as_view(), name='author_update'),
    path('author/delete/<int:pk>', views.AuthorDeleteView.as_view(), name='author_delete'),
    #----------
    path('book/create/', views.BookView.as_view(), name='book_create'),
    path('book/list/', views.BookList.as_view(), name='book_list'),
    path('book/update/<int:pk>', views.BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>', views.BookDeleteView.as_view(), name='book_delete'),
]