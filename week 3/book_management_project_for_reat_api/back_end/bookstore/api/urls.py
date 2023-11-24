from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', views.BookList_viwe,basename="books")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('books/', views.BookList_viwe.as_view(),name = 'book'),
    path('books/<int>:/', views.Book_list_update_or_delete.as_view(),name = 'book_edit'),
]