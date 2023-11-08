
from django.urls import path
from a1.views import home
from .import views
urlpatterns = [
  
   path('',views.home,name = 'home'),
   path('store/',views.store,name='store'),
   path('show/',views.show,name='show'),
   path('edit/<int:id>',views.edit,name='edit'),
   path('delete/<int:id>/',views.delete,name='delete'),
   
]
