

from django.urls import path
from . import views
urlpatterns = [
   path('', views.hello,name="homepage"),
   path('delete/<int:roll>/',views.delete_stu,name='delete_stu'),
   
]
