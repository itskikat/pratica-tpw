from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from app.models import Author, Book, Publisher

# Create your views here.

def renderIndex(request):
    return render(request, 'index.html')

# a) Uma página com a lista dos títulos de todos os livros;
def booksList(request):
    tparams = {
        'all_books': Book.objects.all()
    }
    return render(request, 'books.html', tparams)

def bookDetails(request, b_id):
    tparams = {
        'book': Book.objects.get(id=b_id)
    }
    return render(request, 'bookdetails.html', tparams)


# c) uma página com a lista dos nomes de todos os autores;
def authorsList(request):
    tparams = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'authors.html', tparams)

def authorDetails(request, a_id):
    tparams= {
        'author': Author.objects.get(id=a_id)
    }
    return render(request, 'authordetails.html', tparams)

# e)
def publishersList(request):
    tparams = {
        'all_publishers': Publisher.objects.all()
    }
    return render(request, 'publishers.html', tparams)

def publisherDetails(request, p_id):
    tparams = {
        'publisher': Publisher.objects.get(id=p_id)
    }
    return render(request, 'publisherdetails.html', tparams)

def getAuthorBooks(request, a_name):
    tparams = {
        'author_books': Book.objects.filter(authors__name__contains=a_name)
    }
    return render(request, 'authorbooks.html', tparams)

def getPublisherAuthors(request, p_name):

    if Book.objects.filter(publisher__name__contains=p_name):
        #print(Book.objects.get().authors)
        tparams = {
            'publisher_authors': Book.objects.get().authors
        }
        return render(request, 'publisherauthors.html', tparams)