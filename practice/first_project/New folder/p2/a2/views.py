from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    return HttpResponse("""
                        
                        
                       <h1> this is about page </h1>
                       <a  href  = '/a2/contact/'> CONTACT  </a> <br>
                       <a  href  = '/a3/info/'> info  </a> <br>
                       <a  href  = '/a3/feed_back/'> feed_back  </a>
                        
                        """)


def contact(request):
    return HttpResponse("""
                        
                        this is contact page
                        <a  href  = '/a2/about/'> ABOUT  </a> <br>
                        
                        <a  href  = '/a3/info/'> info  </a> <br>
                       <a  href  = '/a3/feed_back/'> feed_back  </a>
                        
                        """)