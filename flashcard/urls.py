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


urlpatterns = patterns('flashcard.views',

 url(r'list/$',                             'flash_card_list',   name="flash_card_list"),
 url(r'(?P<flash_card_id>\d+)/detail/$',    'flash_card_detail', name="flash_card_detail"), 
 
 url(r'section/(?P<section_id>\d+)/flashcard/add/$',         'flash_card_add',         name="flash_card_add"),
 url(r'section/(?P<section_id>\d+)/flashcard/add/success/$', 'flash_card_add_success', name="flash_card_add_success"),
 url(r'section/(?P<section_id>\d+)/flashcard/next/$',        'flash_card_next',        name="flash_card_next"),
 
 url(r'chapter/(?P<chapter_id>\d+)/flashcard/next/$',        'flash_card_next_chapter', name="flash_card_next_chapter"),
 

)