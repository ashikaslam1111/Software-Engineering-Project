from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>hello this my first my project</h1>")

def about(request):
    return HttpResponse("hello this my about page")