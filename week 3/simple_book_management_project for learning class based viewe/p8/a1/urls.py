
from django.urls import path
from a1.views import home
from .import views
from  django.views.generic import TemplateView
urlpatterns = [
  
   #path('',TemplateView.as_view(template_name ='base.html'),name = 'home'),
   path('<int:roll>/',views.MyTemplateView.as_view(),{'author':'rahim'}),
  # path('store/',views.store,name='store'),
   path('store/',views.Form_show.as_view(),name='store'),
  # path('show/',views.show,name='show'),
   path('show/',views.Show_book.as_view(),name='show'),
  # path('edit/<int:id>',views.edit,name='edit'),
   path('edit_book/<int:pk>/',views.update_book.as_view(),name='edit'),
 #  path('delete/<int:id>/',views.delete,name='delete'),
   path('delete/<int:pk>/',views.Delete_book.as_view(),name='delete'),
   path('book_detail_view/<int:id>/',views.Book_detail.as_view(),name = 'book_detail'),
   
   
]
