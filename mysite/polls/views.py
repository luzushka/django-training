# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

# Create your views here.

def index(request):
    all_albums= Album.objects.all()
    template=loader.get_template('polls/index.html')
    context={
        'all_albums': all_albums,
        }
    return HttpResponse(template.render(context, request))

def detail (request,album_id):
    return HttpResponse("<h2>Details for album id: "+str(album_id) +"</h2>")
