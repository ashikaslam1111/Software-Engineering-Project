from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def menu(request):
    return HttpResponse("""<h1> MENU</h1>
               <br>       <a href = "/a1/galary/">galary</a>  
                  <br>  <a href = "/a2/feedback"> feed back</a> 
                          <br> <a href = "/a2/contact"> contact</a>      """)


def galary(request):
    return HttpResponse("""<h1>GALARY</h1> 
                         <br>       <a href = "/a1/menu/">menu</a>  
                     <br>  <a href = "/a2/feedback"> feed back</a> 
                          <br> <a href = "/a2/contact"> contact</a>    """)