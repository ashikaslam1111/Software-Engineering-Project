from django.urls import path
from. import views
urlpatterns = [
path('menu/',views.menu),
path('galary/',views.galary)
]