from django.db import models

# Create your models here.

class Book_store_model(models.Model):
    CATAGORY = (
        ('Mystery','Mystery'),
        ('Thriller','Thriller'),
        ('Horrror','Horrror'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50,choices= CATAGORY)
    first_pub = models.DateTimeField(auto_now_add=True)# for the first time
    last_pub = models.DateTimeField(auto_now=True)# always
    
    def __str__(self) -> str:
        return self.name
