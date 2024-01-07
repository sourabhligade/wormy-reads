
from django import forms
from .models import Book,Genre

class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('NON-FICTION', 'Non-Fiction'),
        ('AUTOBIOGRAPHY', 'Autobiography'),
        ('NOVELS', 'Novels'),
        ('THRILLERS', 'Thrillers'),
        ('HISTORY', 'History'),
        ('POETRY', 'Poetry'),
    ]

genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'select2'}),
    )