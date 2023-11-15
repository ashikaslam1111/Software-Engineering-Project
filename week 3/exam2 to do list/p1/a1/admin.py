from django.contrib import admin
from a1.models import MyTask

# Register your models here.
@admin.register(MyTask)
class MyTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'first_date', 'last_edit', 'category', 'edit_count', 'status', 'finished_date')


