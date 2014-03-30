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
# along with studyit-flashcard. If not, see <http://www.gnu.org/licenses/gpl-2.0.html.

from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse


def index(request, template_name="index.html"):
    """  
    """
                
    dict = { }
    return render_to_response(template_name, dict,  context_instance=RequestContext(request))

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    odat = {'username': username, }
    return render_to_response('login.html', odat, context_instance=RequestContext(request))



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Pages that REQUIRE user login should be placed in this section.
#    When auditing, make sure all functions that accept "request" as the first parameter have @login_required 
#    at the beginning of the definition.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))