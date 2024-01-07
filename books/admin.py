from django.contrib import admin
from .models import Book
from .forms import BookAdminForm

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
