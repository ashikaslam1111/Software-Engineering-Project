from django.db import models
from django.contrib import admin

class MyTask(models.Model):
    CATEGORY = (
        ('PERSONAL', 'PERSONAL'),
        ('FAMILY', 'FAMILY'),
        ('ACADEMIC', 'ACADEMIC'),
        ('JOB', 'JOB'),
        ('OTHER', 'OTHER')
    )
  
    title = models.CharField(max_length=50)
    description = models.TextField(default='empty')
    first_date = models.DateField(auto_now_add=True)
    last_edit = models.DateField(auto_now=True)
    category = models.CharField(max_length=50, choices=CATEGORY, default='unknown')
    edit_count = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='INCOMPLETED')
    finished_date = models.DateTimeField(null=True, blank=True)
  
    def __str__(self) -> str:
        return self.title


