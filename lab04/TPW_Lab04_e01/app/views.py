from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from app.models import Author, Book, Publisher
from app.forms import BookQueryForm, AuthorQueryForm, BookForm, AuthorForm, PublisherForm
from django.urls import reverse

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


"""
    AULA 04
"""
def info(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>&s</table>' % '\n'.join(html))

def booksearch(request):
    if 'query' in request.POST:
        query = request.POST['query']
        if query:
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'booklist.html', {'books': books, 'query': query})
        else:
            return render(request, 'booksearch.html', {'error': True})
    else:
        return render(request, 'booksearch.html', {'error': False})

def bookquery(request):
    # if POST request, process form data
    if request.method == 'POST':
        # create form instance and pass data to it
        form = BookQueryForm(request.POST)
        if form.is_valid(): # is it valid?
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'booklist.html', {'books': books, 'query': query})
    # if GET (or any other method), create blank form
    else:
        form = BookQueryForm()
    return render(request, 'bookquery.html', {'form': form})

def authorquery(request):
    # if POST request, process form data
    if request.method == 'POST':
        # create form instance and pass data to it
        form = AuthorQueryForm(request.POST)
        if form.is_valid(): # is it valid?
            query = form.cleaned_data['query']
            print(query)
            authors = Author.objects.filter(name__icontains=query)
            print(authors)
            return render(request, 'authorlist.html', {'authors': authors, 'query': query})
    # if GET (or any other method), create blank form
    else:
        form = AuthorQueryForm()
    return render(request, 'authorquery.html', {'form': form})

# 2 c)
def insertbook(request):
    # if POST request, process form data
    if request.method == 'POST':
        # create form instance and pass data to it
        form = BookForm(request.POST)
        if form.is_valid():  # is it valid?
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            authors = form.cleaned_data['authors']
            publisher = form.cleaned_data['publisher']
            new_book = Book.objects.create(title=title, date=date, publisher=publisher)
            for aut in authors:
                new_book.authors.add(aut)
            return HttpResponseRedirect(reverse('insert book form'))
    else:
        form = BookForm()
    return render(request, 'insertbook.html', {'form': form})

def insertauthor(request):
    # if POST request, process form data
    if request.method == 'POST':
        # create form instance and pass data to it
        form = AuthorForm(request.POST)
        if form.is_valid():  # is it valid?
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            new_author = Author.objects.create(name=name, email=email)
            new_form = AuthorForm()
            return render(request, 'insertauthor.html', {'success': True, 'form': new_form})
    else:
        form = AuthorForm()
    return render(request, 'insertauthor.html', {'form': form})

def insertpublisher(request):
    # if POST request, process form data
    if request.method == 'POST':
        # create form instance and pass data to it
        form = PublisherForm(request.POST)
        if form.is_valid():  # is it valid?
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']
            website = form.cleaned_data['website']
            new_publisher = Publisher.objects.create(name=name, city=city, country=country, website=website)
            new_form = PublisherForm()
            return render(request, 'insertpublisher.html', {'success': True, 'form': new_form})
    else:
        form = PublisherForm()
    return render(request, 'insertpublisher.html', {'form': form})
