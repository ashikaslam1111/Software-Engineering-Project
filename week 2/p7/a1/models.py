from django.db import models

# Create your models here.


class StudentMOdel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    fatehr_name = models.CharField(max_length=40)
    address = models.TextField()
    def __str__(self) -> str:
        return self.name