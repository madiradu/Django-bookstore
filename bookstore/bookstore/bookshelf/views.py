from django.shortcuts import render
from bookstore.bookshelf.models import Book
from rest_framework import viewsets
from bookstore.bookshelf.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions as permissions
from rest_framework import renderers

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        book = self.get_object()
        return Response(book.highlighted)

    def perform_create(self, serializer):
        serializer.save()


