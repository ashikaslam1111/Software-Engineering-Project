from django.db import models

# Create your models here.


class StudentMOdel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    fatehr_name = models.CharField(max_length=40)
    address = models.TextField()
    def __str__(self) -> str:
        return self.name
    
    
    
    
class Comoninfo(models.Model):
     name = models.CharField(max_length=40)
     city = models.TextField()
     class Meta:
         abstract = True
         
         
class Studentinfo(Comoninfo):
    slary = models.IntegerField()
    
    
class Teacherinfo(Comoninfo):
    payment = models.IntegerField()
    
    
    
class Employee(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    digicnation = models.CharField(max_length=40)
    
    

class Manager(Employee):
   take_inter_viewe = models.BooleanField()
   hiring = models.BooleanField()
    
    
    
    
class Friend(models.Model):
    name = models.CharField(max_length=40,default='rahim')
    school = models.CharField(max_length=40)
    section = models.CharField(max_length=40)
    class_teacher = models.CharField(max_length=60)
    hw = models.BooleanField()
    atendance = models.BooleanField()
    
       
    class Meta:
        ordering = ['id']
   
    
    
class Me(Friend):
    class Meta:
        proxy = True
        ordering = ['id']
        
        
        
        
        
# for one to one rel

class Person(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
    
class Passport(models.Model):
    user = models.OneToOneField(to=Person,on_delete=models.CASCADE)
    pass_num = models.IntegerField(primary_key=True)
    page = models.IntegerField()
    validity = models.IntegerField()
    
    


# one to many rel

class Post(models.Model):
    
    user = models.ForeignKey(to=Person,on_delete=models.SET_NULL,null=True)# ForeignKey for one to many
    
    cap = models.CharField(max_length=50)
    details = models.CharField(max_length=50)
    


# many to many rel
class Students(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(default=0)
    class_name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name




class Teacher(models.Model):
    stu = models.ManyToManyField(to=Students)
    name = models.CharField(max_length=50)
    subjenct = models.CharField(max_length=30)
    mobile = models.CharField(max_length=11)
    
    def stu_list(self):
        return ','.join([str(i) for i in self.stu.all()])
    
    def __str__(self) -> str:
        return self.name