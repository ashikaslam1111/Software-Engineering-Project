from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def feed_back(request):
    return HttpResponse("""this is the feddback page
                        
                    <a href  = '/a3/info/'> inf </a>   <br> 
                    <a  href  = '/a2/contact/'> CONTACT  </a> <br>
                    <a  href  = '/a2/about/'> ABOUT  </a>
                        
                        """)

def info(requset):
    return HttpResponse("""this is our ifo page
                        
                        <a href = '/a3/feed_back/'> feed_back </a>
                        <br>
                        <a  href  = '/a2/contact/'> CONTACT  </a>
                         <br>
                    <a  href  = '/a2/about/'> ABOUT  </a>
                        """)