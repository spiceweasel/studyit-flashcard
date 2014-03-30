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
from book.models import Section, Chapter, Book

class ObjectOwner(models.Model):
    """    Abstract class used by the Object Views System to delineate owners of objects created in the database.
    """
    object_owner = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related")
    create_timestamp = models.DateTimeField(auto_now_add=True)
    
    _object_name = "ObjectOwner"
    
    class Meta:
        abstract = True

CARD_SKILL_LEVEL = (('a', 'Basic'), ('b', 'Intermdiate'), ('c', 'Advanced'))

class FlashCard(ObjectOwner):
    section = models.ForeignKey(Section)
    
    question = models.TextField(default="", blank=True)
    question_image = models.ImageField(upload_to="flashcard", default="", blank=True)
    
    answer = models.TextField(default="", blank=True)
    answer_image = models.ImageField(upload_to="flashcard", default="", blank=True)
    
    vote_average = models.SmallIntegerField(blank=True, default=0)  # totaled by the system
    
    card_skill_level = models.CharField(max_length=1, default="b", choices=CARD_SKILL_LEVEL)
    
    def question_short(self):
        if self.question: return self.question[0:50]
    def __unicode__(self):
        if self.question: return self.question
        return "Image Question"
    

class FlashCardVote(ObjectOwner):
    flash_card = models.ForeignKey(FlashCard)
    vote = models.SmallIntegerField()
    
class FlagType(models.Model):
    """
        Inappropriate Material, out of context, wrong answer
    """
    name = models.CharField(max_length=30)
    
    def __unicode__(self): return self.name
    
class FlashCardFlag(ObjectOwner):
    flag_type = models.ForeignKey(FlagType)
    flash_card = models.ForeignKey(FlashCard)
    note = models.TextField(default="")
    
    def __unicode__(self): return self.flag_type.name + " " + self.note[0:50]
    
FLASH_CARD_RESPONSE_TYPE = (('A', 'Correct'), ('B', 'Incorrect'),)
    
class CardUserResponse(ObjectOwner):
    flash_card = models.ForeignKey(FlashCard)
    response_type = models.CharField(max_length=1, choices=FLASH_CARD_RESPONSE_TYPE)
    
# class LessonSet(ObjectOwner):
#     book = models.ForeignKey(Book)
#     title = models.CharField(max_length=40)
#     
#     def __unicode__(self): return self.title
    
# class LessonFlashCard(models.Model):
#     lesson_set = models.ForeignKey(LessonSet)
#     flash_card = models.ForeignKey(FlashCard)
#     
#     def __unicode__(self): return self.lesson_set.title + " " + self.flash_card.__unicode__()
    
    