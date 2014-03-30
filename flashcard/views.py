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

from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.forms import ModelForm

from flashcard.models import FlashCard, CardUserResponse, FlagType, FlashCardFlag, FlashCardVote
from flashcard.forms import FlashCardForm
from book.models import Section




@login_required
def flash_card_list(request, template_name="flashcard/flash_card_list.html"):
    
    cards = FlashCard.objects.all()
    
    gets = request.GET.copy()
    
    try: sect = Section.objects.get(pk=int(gets['section']))
    except: sect = None
    
    if sect: cards = cards.filter(section=sect)
    
    dict = {'flash_cards': cards, 'section': sect }
    return render_to_response(template_name, dict, context_instance=RequestContext(request))

@login_required
def flash_card_add_success(request, section_id=0):
    return flash_card_add(request, section_id=section_id, message="Flash card added successfully.")
    
@login_required
def flash_card_add(request, section_id=0, message="", template_name="flashcard/flash_card_add.html"):
    
    sect = get_object_or_404(Section, pk=int(section_id))
    
    form = None
    form = FlashCardForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        fc = form.save(commit=False)
        fc.object_owner = request.user
        fc.section = sect
        fc.save()
        try: sub = request.POST['submit']
        except: sub = ""
        
        if sub == "Save and add another": return HttpResponseRedirect(reverse('flashcard.views.flash_card_add_success', kwargs={'section_id': sect.id,}))
            
        return HttpResponseRedirect(reverse('book.views.book_view', kwargs={'book_id': sect.chapter.book.isbn }))
    
    dict = {'section': sect, 'form': form, 'message': message }
    return render_to_response(template_name, dict, context_instance=RequestContext(request))

@login_required
def flash_card_detail(request, flash_card_id=0, by_chapter=False, template_name="flashcard/flash_card_detail.html"):
    
    card = get_object_or_404(FlashCard, pk=flash_card_id)
    
    dict = {'flash_card': card, 'by_chapter': by_chapter }
    return render_to_response(template_name, dict, context_instance=RequestContext(request))

@login_required
def flash_card_next(request, section_id=0, template_name="flashcard/flash_card_detail.html"):
    
    sect = get_object_or_404(Section, pk=section_id)
    
    card = get_object_or_404(FlashCard, pk=int(request.GET['flash_card']))
    
    cresponse = CardUserResponse(object_owner=request.user, flash_card=card)
    response_type = None
    try: 
        rt = request.GET['correct']
        if rt: response_type = "A"
    except:
        try:
            rt = request.GET['incorrect']
            if rt: response_type = "B"
        except: pass
    if response_type != None:
        cresponse.response_type = response_type
        #TODO:  we are not saving until the rest of the functionality that uses this is implemented.
        #cresponse.save()
    
    def get_next_card():
        cards = FlashCard.objects.filter(section=card.section).order_by('?')
        if cards: return cards[0]
    
    next_card = get_next_card()
    cnt = 0
    while ((next_card.id == card.id) and (cnt <= 4)):
        next_card = get_next_card()
        cnt += 1
       
    return flash_card_detail(request, next_card.id)


@login_required
def flash_card_next_chapter(request, chapter_id=0, template_name="flashcard/flash_card_detail.html"):
    from book.models import Chapter
    chapt = get_object_or_404(Chapter, pk=chapter_id)
    
    try: card = FlashCard.objects.get(id=int(request.GET['flash_card']))
    except: card = None
    
    
    try: cresponse = CardUserResponse(object_owner=request.user, flash_card=card)
    except: cresponse = None
    response_type = None
    
    try: 
        rt = request.GET['correct']
        if rt: response_type = "A"
    except:
        try:
            rt = request.GET['incorrect']
            if rt: response_type = "B"
        except: pass
    if response_type != None and cresponse != None:
        cresponse.response_type = response_type
        #TODO:  we are not saving until the rest of the functionality that uses this is implemented.
        #cresponse.save()
    
    def get_next_card():
        cards = FlashCard.objects.filter(section__chapter=chapt).order_by('?')
        if cards: return cards[0]
    
    next_card = get_next_card()
    
    if card:
        cnt = 0
        while ((next_card.id == card.id) and (cnt <= 4)):
            next_card = get_next_card()
            cnt += 1
       
    return flash_card_detail(request, next_card.id, by_chapter=True)

@login_required
def get_next_from_section(request, section_id=0, template_name="flashcard/get_next_from_section.html"):
    """ Management control panel. 
    """
    from student.models import StudentMajor
    
    dept = get_object_or_404(Department, pk=department_id)
    
    majors = MajorCourseOfStudy.objects.filter(department=dept, is_approved=True, is_obsolete=False)
    smajor = StudentMajor.objects.filter(is_current=True, major_course_of_study__in=majors)
    
    dict = {'department': dept, 'student_majors': smajor }
    return render_to_response(template_name, dict, context_instance=RequestContext(request))