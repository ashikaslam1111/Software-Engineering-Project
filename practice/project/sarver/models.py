from django.db import models


#Create a Models Class
class Login_from(models.Model):
    Username = models.CharField(max_length=20)
    Password = models.IntegerField()

    