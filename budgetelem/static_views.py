# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

def about(request):

    return render_to_response('static/about.html')

def help(request):

    return render_to_response('static/help.html')

def helpdoc(request):

    return render_to_response('static/helpdoc.html')

def contacts(request):

    return render_to_response('static/contacts.html')

def intentions(request):

    return render_to_response('static/intentions.html')

def donate(request):

    return render_to_response('static/donate.html')
