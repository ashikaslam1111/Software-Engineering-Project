

from django.urls import path
from a1.views import home,show

urlpatterns = [
    path('', home ),
    path('show/', show),
]
