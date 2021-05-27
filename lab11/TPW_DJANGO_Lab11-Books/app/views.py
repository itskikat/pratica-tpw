from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.searializers import AuthorSerializer, PublisherSerializer, BookSerializer
from app.models import *

# Create your views here.

# web service to get specific author
@api_view(['GET'])
def get_author(request):
    id = int(request.GET['id'])
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)

# web service to get a list of authors
@api_view(['GET'])
def get_authors(request):
    authors = Author.objects.all()
    if 'num' in request.GET:
        num = int(request.GET['num'])
        authors = authors[:num]
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)

# web service to create an author
@api_view(['POST'])
def create_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# web service to update an author
@api_view(['PUT'])
def update_author(request):
    id = request.data['id']
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AuthorSerializer(author, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# web service to delete an author
@api_view(['DELETE'])
def del_author(request, id):
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    author.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

'''
    PUBLISHERS
'''
# web service to get specific publisher
@api_view(['GET'])
def get_publisher(request):
    id = int(request.GET['id'])
    try:
        publisher = Publisher.objects.get(id=id)
    except Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PublisherSerializer(publisher)
    return Response(serializer.data)

# web service to get a list of publishers
@api_view(['GET'])
def get_publishers(request):
    publishers = Publisher.objects.all()
    if 'num' in request.GET:
        num = int(request.GET['num'])
        publishers = publishers[:num]
    serializer = PublisherSerializer(publishers, many=True)
    return Response(serializer.data)

# web service to create a publisher
@api_view(['POST'])
def create_publisher(request):
    serializer = PublisherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# web service to update a publisher
@api_view(['PUT'])
def update_publisher(request):
    id = request.data['id']
    try:
        publisher = Publisher.objects.get(id=id)
    except Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PublisherSerializer(publisher, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# web service to delete a publisher
@api_view(['DELETE'])
def del_publisher(request, id):
    try:
        publisher = Publisher.objects.get(id=id)
    except Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    publisher.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

'''
    BOOKS
'''
# web service to get specific book
@api_view(['GET'])
def get_book(request):
    id = int(request.GET['id'])
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book)
    return Response(serializer.data)

# web service to get a list of books
@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    if 'num' in request.GET:
        num = int(request.GET['num'])
        books = books[:num]
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# web service to create a book
@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# web service to update a book
@api_view(['PUT'])
def update_book(request):
    id = request.data['id']
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# web service to delete a book
@api_view(['DELETE'])
def del_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)