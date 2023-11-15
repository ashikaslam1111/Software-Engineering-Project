
from django.urls import path
from.import views
urlpatterns = [
   path('',views.signup,name='signup'),
   path('login/',views.Login,name='login'),
   path('profile/',views.profile,name = 'profile'),
   path('logout/',views.user_logout,name='logout'),
   path('passchange/',views.pass_change,name = 'passchange'),
   path('passchange2/',views.pass_change2,name = 'passchange2'),
   path('edit/',views.edit_data,name = 'edit_data'),
  
]
