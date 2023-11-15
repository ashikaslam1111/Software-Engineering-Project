from django.contrib import admin

# Register your models here.
from a1.models import Teacher,Students,Post,StudentMOdel,Studentinfo,Teacherinfo,Employee,Manager,Friend,Me,Person ,Passport

# class list_show(admin.ModelAdmin):
#     list_display = ('name')

admin.site.register(StudentMOdel)
# admin.site.register(Studentinfo)
# admin.site.register(Teacherinfo)
# admin.site.register(Manager)
# admin.site.register(Employee)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','digicnation']
    
    
    
@admin.register(Manager)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','digicnation','take_inter_viewe','hiring']


@admin.register(Friend)

class FriendAdmin(admin.ModelAdmin):
    list_display = ['id','name','school','section','class_teacher','atendance','hw']


@admin.register(Me)

class MeAdmin(admin.ModelAdmin):
    list_display = ['id','name','school','section','class_teacher','atendance','hw']
    
    
    
@admin.register(Person)

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','email']
    

@admin.register(Passport)

class PassportAdmin(admin.ModelAdmin):
    list_display = ['pass_num','user','page','validity']
    
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user','cap','details']
    
@admin.register(Teacher)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name','subjenct','mobile','stu_list']
    
@admin.register(Students)

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name','roll','class_name']






#  username   ashikaslam1111@gamil.com
