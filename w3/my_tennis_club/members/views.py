

from django.shortcuts import render 
from django.http import HttpResponse
from django.template import loader

def members(request):
    temp = loader.get_template('myfirst.html')
    return HttpResponse(temp.render())
