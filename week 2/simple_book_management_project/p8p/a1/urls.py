
from django.urls import path
from .import views

urlpatterns = [
   path('',views.home,name='home'),
   path('show/',views.show_data,name='show'),
   path('store/',views.store,name='store'),
   path('delete/<int:id>',views.delete,name ='delete'),
   path('edit/<int:id>/',views.edit,name='edit'),
]
