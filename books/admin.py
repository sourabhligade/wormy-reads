from django.contrib import admin
from .models import Book,Wishlist
from .forms import BookAdminForm
from django.contrib import admin


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm



class WishlistAdmin(admin.ModelAdmin):
    # Customizations go here
    list_display = ('user', 'get_books')

    def get_books(self, obj):
        return ", ".join([book.title for book in obj.books.all()])
    get_books.short_description = 'Books'

admin.site.register(Wishlist, WishlistAdmin)
