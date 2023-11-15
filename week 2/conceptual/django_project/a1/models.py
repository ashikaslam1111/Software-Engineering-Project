from django.db import models
from django.urls import reverse
# Create your models here.


from django.urls import reverse  # Import necessary for reverse function

class Post(models.Model):
    title = models.CharField(max_length=200)  # Corrected 'tittle' to 'title'
    author = models.ForeignKey(
        "auth.User",  # Corrected 'auth.user' to 'auth.User'
        on_delete=models.CASCADE,  # Corrected parameter name to 'on_delete'
    )
    body = models.TextField() 

    def __str__(self) -> str:
        return self.title  # Corrected 'tittle' to 'title'

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
