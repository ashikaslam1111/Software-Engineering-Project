from django.urls import path
from.import views
urlpatterns = [
   path("info/",views.info),
   path("feed_back/",views.feed_back),
   
]