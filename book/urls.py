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

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('book.views',
  
  url(r'(?P<book_id>\d+)/view/$', 'book_view', name="book_view"),
  url(r'list/$',                  'book_list', name="book_list"),
  url(r'search/$',                'book_search', name="book_search"),
  url(r'categories/$',            'book_categories', name="book_categories"),
  
  #url(r'(?P<chapter_id>\d+)/list/^$', 'chapter_list', name="chapter_list"),
  url(r'chapter/(?P<chapter_id>\d+)/outline/^$', 'chapter_outline', name="chapter_outline"),
  


)