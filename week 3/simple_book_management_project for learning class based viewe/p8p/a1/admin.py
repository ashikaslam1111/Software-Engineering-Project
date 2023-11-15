from django.contrib import admin
from. import models
# Register your models here.
class list_show(admin.ModelAdmin):
    list_display = ('id','name','catogory','first_pub','last_pub')

admin.site.register(models.Book_modle,list_show)