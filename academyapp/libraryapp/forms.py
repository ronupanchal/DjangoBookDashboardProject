from django.forms import models
from .models import Genre, Language, Author, Book


class GenreForm(models.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"


class LanguageForm(models.ModelForm):
    class Meta:
        model = Language
        fields = "__all__"


class AuthorForm(models.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class BookForm(models.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"