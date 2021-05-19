"""TPW_Lab03_e01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.renderIndex, name="index"),
    path('admin/', admin.site.urls),
    path('books/', views.booksList, name="books"),
    path('book/<int:b_id>', views.bookDetails, name="book details"),
    path('authors/', views.authorsList, name="authors"),
    path('author/<int:a_id>', views.authorDetails, name="author details"),
    path('publishers/', views.publishersList, name="publishers"),
    path('publisher/<int:p_id>', views.publisherDetails, name="publisher details"),
    path('abooks/<str:a_name>', views.getAuthorBooks, name="author books"),
    path('pauthors/<str:p_name>', views.getPublisherAuthors, name="publisher authors"),
]
