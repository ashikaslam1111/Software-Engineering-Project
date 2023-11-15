from django.db import models

# Create your models here.

class Book_modle(models.Model):
    CHATAGORY = (('THRILLER','THRILLER'),  ('HORROR','HORROR'))
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    catogory = models.CharField(max_length=50,choices= CHATAGORY)
    first_pub = models.DateField(auto_now_add=True)
    last_pub = models.DateField(auto_now=True)
    def __str__(self) -> str:
        return self.name
    
