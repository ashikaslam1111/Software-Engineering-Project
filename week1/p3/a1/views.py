from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,'f1/about.html',context={
        'author':"hochimih"
    })
    
def home(request):
    return render(request,'f1/home.html',context={
        'autohor':'phitron','Age':19,
        'course':[{'name':'aslam','age':18,'roll':10} ,                                             
        {'name':'monir','age':14,'roll':30} ,
        {'name':'pappu','age':8,'roll':101} ],                                               
  'marks':15, "nam":"aslam mia" ,
  "blog":"hello world thsis ashik aslam from bangladesh"})


def data(request):
    return render(request,"f1/course.html",context={'roll':20})