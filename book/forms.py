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
# along with studyit-flashcard. If not, see <http://www.gnu.org/licenses/gpl-2.0.html>.from django import forms
from book.models import Book

class BookSearchForm(forms.Form):
    isbn = forms.CharField(max_length=13, required=False)
    title = forms.CharField(max_length=100, required=False)
    edition = forms.CharField(max_length=25, required=False)
    authors = forms.CharField(max_length=100, required=False)
    publisher = forms.CharField(max_length=100, required=False)
