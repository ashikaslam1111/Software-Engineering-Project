from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime,timedelta



# Create your views here.

def home(request):# to set cookie
    
  response =  render(request,'home.html')
  #response.set_cookie('name','aslam',max_age=60) # here it works like key value pair 'name' is the key  i mean act like dic in py or map in  cpp
  response.set_cookie('name','aslam',expires=datetime.utcnow()+timedelta(days=7)) # here it works like key value pair 'name' is the key  i mean act like dic in py or map in  cpp
  return response

def get_cookie(request):# can not get cooie from the same html file whire i set it goota make anoter to get it
    
    name = request.COOKIES.get('name')
    print(name)
    return render(request,'get_cookie.html',{'name':name})


def del_cooki(request):# need anothr html
     response =  render(request,'del.html')
     response.delete_cookie('name')
     return response
   
   
   
# sesson 

def set_session(request):
  data = {
    
    'name':'rahim',
    'age':32,
    'language':'bangle',
    
  }
  request.session.update(data)
  # To get the session age (in seconds)
  print(request.session.get_expiry_age())

# To get the session expiry date
  print(request.session.get_expiry_date())

  return render(request,'home.html')


def get_session(request):
   if 'name' in request.session:
      name = request.session.get('age','unknown')# here unknown for when there is no name feild or i delete it
      request.session.modified = True
      return render(request,'session.html',{'name':name})
    
   else:
     return HttpResponse('login agin')


def dEl_sess(request):
 # del request.session['name']
  request.session.flush()
  request.session.clear_expired()
  
  return render(request,'del_sess.html')
