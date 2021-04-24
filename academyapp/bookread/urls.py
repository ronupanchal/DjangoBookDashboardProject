from django.urls import path
from . import views

app_name='bookreadapp'

urlpatterns =[
    #path('', views.bookshow, name='bookshow'),
    path('displaybook/<int:pk>/', views.DisplayBook.as_view(), name='book_display'),
    ]