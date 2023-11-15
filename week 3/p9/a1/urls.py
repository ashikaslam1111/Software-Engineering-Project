"""
URL configuration for p9 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.views.generic import TemplateView
from django.urls import path
from a1.views import dEl_sess,home,get_cookie,del_cooki,set_session,get_session
urlpatterns = [
   # path('', TemplateView.as_view(template_name='home.html')),
   path('',set_session,name='home'),
   path('get/',get_cookie,name='get'),
   path('del/',del_cooki,name='del'),
   path('sess/',get_session),
   path('del_sess/',dEl_sess),
]

