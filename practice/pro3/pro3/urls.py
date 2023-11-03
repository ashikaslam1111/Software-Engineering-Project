
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from.import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('a1/',include('a1.urls')),
    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
