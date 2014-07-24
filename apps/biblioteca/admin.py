#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Publisher, Author, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    filter_horizontal = ('authors',)



# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)

