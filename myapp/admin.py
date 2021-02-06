from django.contrib import admin
from .models import Book, BRMuser
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'author', 'publisher']

admin.site.register(BRMuser)
