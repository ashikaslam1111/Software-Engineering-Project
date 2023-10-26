from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse("""<h1>HOME</h1><br>""")


def ht(request):
    return render(request,'index.html')

