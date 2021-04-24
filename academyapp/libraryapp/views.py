from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from .forms import GenreForm, LanguageForm, AuthorForm, BookForm
from .models import Genre, Language, Author, Book
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    title ="Dashboard"
    totalgenre = Genre.objects.filter().count()
    totallanguage = Language.objects.filter().count()
    totalauthor = Author.objects.filter().count()
    totalbook = Book.objects.filter().count()
    context={
        'title': title,
        'totalgenre': totalgenre,
        'totallanguage': totallanguage,
        'totalauthor': totalauthor,
        'totalbook': totalbook
    }
    return render(request, 'academy/dashboard.html', context )

#------------Start Genre--------------------------------
class GenreView(View):

    def get(self, request):
        form = GenreForm()
        return render(request, 'academy/genre_create.html', {'form':form})

    def post(self, request):
        if request.method == 'POST':
            form = GenreForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data['name'])
                form.save()
                return redirect('academy:genre_list')


class GenreList(ListView):
    model = Genre
    template_name = 'academy/genre.html'
    context_object_name = 'genres'


class GenreUpdateView(UpdateView):
    # specify the model you want to use
    model = Genre
    template_name = 'academy/genre_form.html'
    # specify the fields
    fields = [
        "name"
    ]
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = reverse_lazy('academy:genre_list')


class GenreDeleteView(DeleteView):
    # specify the model you want to use
    model = Genre
    template_name = 'academy/genre_confirm_delete.html'
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = reverse_lazy('academy:genre_list')

#------------End Genre--------------------------------


#------------Start Language--------------------------------
class LanguageView(View):

    def get(self, request):
        form = LanguageForm()
        return render(request, 'academy/language_create.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = LanguageForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data['name'])
                form.save()
                return redirect('academy:language_list')


class LanguageList(ListView):
    model = Language
    template_name = 'academy/language.html'
    context_object_name = 'languages'


class LanguageUpdateView(UpdateView):
    # specify the model you want to use
    model = Language
    template_name = 'academy/language_form.html'
    # specify the fields
    fields = [
        "name",
    ]
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = reverse_lazy('academy:language_list')


class LanguageDeleteView(DeleteView):
    # specify the model you want to use
    model = Language
    template_name = 'academy/language_confirm_delete.html'
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = reverse_lazy('academy:language_list')

#---------------End Language------------------


#------------Start Author--------------------------------
class AuthorView(View):

    def get(self, request):
        form = AuthorForm()
        return render(request, 'academy/author_create.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = AuthorForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data['first_name'])
                form.save()
                return redirect('academy:author_list')


class AuthorList(ListView):
    model = Author
    template_name = 'academy/author.html'
    context_object_name = 'authors'


class AuthorUpdateView(UpdateView):
    # specify the model you want to use
    model = Author
    template_name = 'academy/author_form.html'
    # specify the fields
    fields = [
        "first_name",
        "last_name",
        "date_of_birth",
        "date_of_death",
    ]
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = reverse_lazy('academy:author_list')


class AuthorDeleteView(DeleteView):
    # specify the model you want to use
    model = Author
    template_name = 'academy/author_confirm_delete.html'
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = reverse_lazy('academy:author_list')
#---------------End Author------------------


#------------Start Book--------------------------------
class BookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'academy/book_create.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = BookForm(request.POST, request.FILES)
            if form.is_valid():
                #print(form.cleaned_data['title'])
                form.save()
                return redirect('academy:book_list')


class BookList(ListView):
    model = Book
    template_name = 'academy/book.html'
    context_object_name = 'books'


class BookUpdateView(UpdateView):
    # specify the model you want to use
    model = Book
    template_name = 'academy/book_form.html'
    # specify the fields
    fields = [
        "title",
        "author",
        "language",
        "genre",
        "isbn",
        "summary",
        "file",
    ]
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = reverse_lazy('academy:book_list')


class BookDeleteView(DeleteView):
    # specify the model you want to use
    model = Book
    template_name = 'academy/book_confirm_delete.html'
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = reverse_lazy('academy:book_list')
#---------------End Book------------------

