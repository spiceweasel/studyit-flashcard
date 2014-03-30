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

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse

from book.models import Book, Chapter, Section

@login_required
def book_view(request, book_id=None, template_name="book/book_view.html"):
    
    book = get_object_or_404(Book, pk=book_id)
    
    dict = {'book': book, }
    return render_to_response(template_name, dict, context_instance=RequestContext(request))

@login_required
def book_categories(request, template_name="book/book_categories.html"):
    from book.models import BookCategory
    
    cat_id = request.GET.get("category_id", 0)
    
    if cat_id: return book_list(request)
    else: categories = BookCategory.objects.filter(parent=None)
    
    dict = {'categories': categories, }
    return render_to_response(template_name, dict, context_instance=RequestContext(request))

@login_required
def book_list(request, template_name="book/book_list.html"):
    
    gets = request.GET.copy()
    cat_id = gets.get("category_id", 0)
    
    if cat_id: books = Book.objects.filter(category=cat_id) 
    else: 
        books = Book.objects.all()
        #TODO: fix this and add a pagination method
        if books: books = books.filter()[0:50]
    
    dict = {'books': books, }
    return render_to_response(template_name, dict, context_instance=RequestContext(request))

@login_required
def book_search(request, template_name="book/book_search.html"):
    from book.forms import BookSearchForm
    
    books = []
    
    frm = BookSearchForm(request.POST or None)
    if frm.is_valid():
        books = Book.objects.all()
        cln = frm.cleaned_data
        if cln['isbn'] != "": books = books.filter(isbn__icontains=cln['isbn'])
        if cln['title'] != "": books = books.filter(title__icontains=cln['title'])
        if cln['edition'] != "": books = books.filter(edition__icontains=cln['edition'])
        if cln['authors'] != "": books = books.filter(authors__icontains=cln['authors'])
        if cln['publisher'] != "": books = books.filter(publisher__icontains=cln['publisher'])
    
    
    dict = {'books': books, 'form': frm }
    return render_to_response(template_name, dict, context_instance=RequestContext(request))

@login_required
def chapter_outline(request, chapter_id=0, template_name="book/chapter_outline.html"):
    
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    
    dict = {'chapter': chapter, }
    return render_to_response(template_name, dict, context_instance=RequestContext(request))