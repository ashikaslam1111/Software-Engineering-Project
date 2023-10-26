from django.shortcuts import render

# Create your views here.
def home(retuest):
    return render(retuest,'./f1/index.html',context={'autohor':'phitron','Age':19,
                                                     
                                                 'course':[
                                              {'name':'aslam','age':18,'roll':10} ,                                             
                                                               {'name':'monir','age':14,'roll':30} ,                             
                                                                                            
                                                {'name':'pappu','age':8,'roll':101} ]  ,    
                                                     
                                                     
                                                     
  'marks':15,      "nam":"aslam mia"  ,"blog":"hello world thsis ashik aslam from bangladesh"                                            })