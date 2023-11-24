from django.shortcuts import render

# Create your views here.


from .models import Book_modle
from .serializers import BookstoreSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# class BookList_viwe(APIView): # sobgula dekhar joono 
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         model = Book_modle.objects.all()
#         serializer = BookstoreSerializer(model, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer =  BookstoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# api view long : metho 1

# class Book_list_update_or_delete(APIView): # ekta dekhar jonno 
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Book_modle.objects.get(pk=pk)
#         except Book_modle.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = BookstoreSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer =BookstoreSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)







#contrip api view method 2






from rest_framework import generics


class SnippetList(generics.ListCreateAPIView): # get and post request
    queryset = Book_modle.objects.all()
    serializer_class = BookstoreSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView): # update and delete 
    queryset = Book_modle.objects.all()
    serializer_class = BookstoreSerializer






