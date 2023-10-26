from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def contact(request):
    
    return HttpResponse("""<h1>CONTACT</h1>
                    <br>
                    <a href = "/a2/feedback"> feed back</a>
                        <br>       <a href = "/a1/galary/">galary</a>  
                          <br>       <a href = "/a1/menu/">menu</a>
                        """)


def fedd_back(request):
     return HttpResponse("""<h1>FEED BACK</h1>
                         <br>
                    <a href = "/a2/contact"> contact</a>
                         <br>       <a href = "/a1/galary/">galary</a>  
                          <br>       <a href = "/a1/menu/">menu</a>
                         """)
    
    