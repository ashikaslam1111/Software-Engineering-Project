from django import forms
from . import models


class Book_form(forms.ModelForm):
    class Meta:
        model = models.Book_modle
        fields =['id','name','catogory']
       