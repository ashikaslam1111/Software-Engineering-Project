from django.shortcuts import render

# Create your views here.

print('hello 1')
def contact(request):
    return render(request,"f1/index.html")
