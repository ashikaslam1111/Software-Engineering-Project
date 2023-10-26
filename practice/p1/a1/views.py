from django.shortcuts import render

from django.http import HttpResponse

def menu(request):
    return HttpResponse("""<h1>MENU</h1><br>""")
