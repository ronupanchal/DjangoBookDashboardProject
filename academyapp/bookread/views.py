from django.shortcuts import render
from django.views import View
from libraryapp.models import Book
from django.views.generic.detail import DetailView
# Create your views here.


def bookview(request):
    title ="Book Reader View"
    return render(request, 'book_read/bookview.html', {'title': title})


class DisplayBook(DetailView):
    model = Book
    template_name = 'book_read/showbook.html'
    print(id)
