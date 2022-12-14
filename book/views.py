from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import *
# Create your views here.


class BooksView(ListCreateAPIView):

    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[IsAuthenticated]


class BookDetails(RetrieveDestroyAPIView):

    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]