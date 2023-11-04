from django.shortcuts import render,HttpResponsePermanentRedirect
from sarver.forms import user

#Create Your Views File
def views_from(request):
    if request.method == 'POST':
        frm = user(request.POST)
        if frm.is_valid():
            return HttpResponsePermanentRedirect('/super/submit')
     
        
    else:
        frm = user()
        print('Get Statemnet')
    return render(request, 'exple/index.html', {'fme' : frm})








