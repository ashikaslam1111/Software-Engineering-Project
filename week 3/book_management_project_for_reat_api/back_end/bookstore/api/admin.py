from django.contrib import admin
from . models import Book_modle

# Register your models here.

class List_show(admin.ModelAdmin):
    list_display =  list_display = ('id','name','catogory','first_pub','last_pub')
    
    
admin.site.register(Book_modle,List_show)
