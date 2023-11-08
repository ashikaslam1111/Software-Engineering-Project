from django.contrib import admin
from . import models
# Register your models here.

class list_show(admin.ModelAdmin):
    list_display = ('id','name','author','catagory','first_pub','last_pub')



admin.site.register(models.Book_store_model , list_show)
