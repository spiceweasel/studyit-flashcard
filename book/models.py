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

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BookCategory(models.Model):
    parent = models.ForeignKey('BookCategory', null=True, blank=True)
    name = models.CharField(max_length=30)
    _book_count = None
    def __unicode__(self): return self.full_name()
    def full_name(self):
        if self.parent: return self.parent.full_name() + '>' + self.name
        return self.name
    def book_count(self):
        
        if self._book_count == None: self._book_count = self.book_set.all().count() 
        return self._book_count
    
    def children(self): return BookCategory.objects.filter(parent=self.id)

class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13)
    title = models.CharField(max_length=100, db_index=True)
    edition = models.CharField(max_length=25)
    authors = models.CharField(max_length=100, db_index=True)
    publisher = models.CharField(max_length=100, db_index=True)
    publication_date = models.DateField()
    
    category = models.ManyToManyField(BookCategory)
    
    def __unicode__(self):
        return self.title
    
class Chapter(models.Model):
    book = models.ForeignKey(Book)
    number = models.SmallIntegerField()
    title = models.CharField(max_length=100, db_index=True)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ('number',)

class Section(models.Model):
    chapter = models.ForeignKey(Chapter)
    number = models.SmallIntegerField()
    title = models.CharField(max_length=125, blank=True, default="")
    page = models.IntegerField(blank=True, default=None, null=True)
    
    def __unicode__(self):
        return "%i" % self.number
    
    class Meta:
        ordering = ('number',)
