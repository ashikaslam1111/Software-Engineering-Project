from django.http import HttpResponse
from django.shortcuts import render
def home(requese):
    
    return HttpResponse ("""<h1>HOME</h1>
                          <br>       <a href = "/a1/galary/">galary</a>  
                          <br>       <a href = "/a1/menu/">menu</a> 
                          <br>  <a href = "/a2/feedback"> feed back</a> 
                          <br> <a href = "/a2/contact"> contact</a> """)


def wellcome(request):
    return render(request,'index.html')





























