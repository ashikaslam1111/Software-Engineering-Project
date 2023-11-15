from django.shortcuts import render,redirect
from a1.forms import RegisterForm
from django.http import HttpResponse
from django import forms
from django.contrib import messages
from a1.forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from a1.forms import Change_userdata
# Create your views here.


def signup(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account created successfully!')
            form.save(commit=True)
            print(form.cleaned_data)
           
        
    else:
        form = RegisterForm()
    return render(request,'./signup.html',{'form':form})






# def login(request):
#    if request.method == 'POST':
#        form = LoginForm(request.POST)
#        if form.is_valid():
#            usr = form.cleaned_data['user_name']
#            pss = form.cleaned_data['password']
          
       
      
   
   
#    else:
#        form = LoginForm()
#    return render(request,'login.html',{'form':form})
   
   
def Login(request):
   if request.method == 'POST':
       form = AuthenticationForm(request=request,data = request.POST )
       if form.is_valid():
            usr = form.cleaned_data['username']
            pss = form.cleaned_data['password']
            user =  authenticate(username=usr,password=pss)# chacing with built is sysmtem that this is valied user
            
            if user is not None:
               
                login(request,user)# ei login inkintu upore inport kora lonig 
                return redirect('profile')
                
                
   else:  form = AuthenticationForm()
   return render(request,'login.html',{'form':form})
       
                
                
            
            
           
def profile(request):
    if  request.user.is_authenticated: 
       return render(request,'profile.html',{'user':request.user})  
    else: return redirect('login')
        





def user_logout(request):
    logout(request)  
    return redirect('login')






def pass_change(request):
    if request.method == 'POST':
        form =PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            update_session_auth_hash(request,form.user) # or form.cleaned_data['user']
            return redirect('profile')
        
    else: form =PasswordChangeForm(user=request.user)
    return render(request,'pass_chang.html',{'form':form}) 




def pass_change2(request):
    if request.method == 'POST':
        form =SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            update_session_auth_hash(request,form.user) # or form.cleaned_data['user']
            return redirect('profile')
        
    else: form =SetPasswordForm(user=request.user)
    return render(request,'pass_chang.html',{'form':form}) 




def edit_data(request): 
    
    if request.method == 'POST':
        form = Change_userdata(request.POST,instance=request.user)
        if form.is_valid():
            form.save(commit=True)
           
            return redirect('profile')
        
    else: form =Change_userdata(instance=request.user)
    return render(request,'pass_chang.html',{'form':form}) 
    
          