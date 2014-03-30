# studyit-flashcard is a django based flashcard system designed for studying on the go.
# Copyright (C) 2013 Scott Jacovidis
# 
# This file is part of studyit-flashcard.
# 
# Studyit-flashcard is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
# 
# Studyit-flashcard is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with studyit-flashcard. If not, see <http://www.gnu.org/licenses/gpl-2.0.html>.
from django.contrib import admin

from book.models import Chapter, Section, Book, BookCategory

class SectionInline(admin.TabularInline):
    model = Section
    extra = 3
    
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('book', 'number', 'title' )
    list_filter = ('book__title',)
    search_fields = ('book__isbn', 'book__title')
    inlines = (SectionInline,)
admin.site.register(Chapter, ChapterAdmin)


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    #list_filter = ("parent",)
    raw_id_fields = ('parent',)
admin.site.register(BookCategory, BookCategoryAdmin)

class SectionAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'number', 'title')
admin.site.register(Section, SectionAdmin)

class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 3
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'isbn' )
    inlines = (ChapterInline,)
admin.site.register(Book, BookAdmin)