from django import forms
from app.models import Author, Book, Publisher

# Create your forms here
class BookQueryForm(forms.Form):
    query = forms.CharField(label='Search:', max_length=100)

class AuthorQueryForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class BookForm(forms.Form):
    title = forms.CharField(label='Title:', max_length=100)
    date = forms.DateField(widget=forms.SelectDateWidget())
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), widget=forms.CheckboxSelectMultiple)
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())

class AuthorForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    email = forms.EmailField()

class PublisherForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    city = forms.CharField(label='City:', max_length=50)
    country = forms.CharField(label='Country:', max_length=50)
    website = forms.URLField()