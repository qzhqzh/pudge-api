from django.contrib import admin
from .models import Blog, Note


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'category')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'category')
