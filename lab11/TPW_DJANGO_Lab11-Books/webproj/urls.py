"""webproj URL Configuration

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
    path('admin/', admin.site.urls),

    # web services
    path('ws/author', views.get_author),
    path('ws/authors', views.get_authors),
    path('ws/authorcre', views.create_author),
    path('ws/authorupd', views.update_author),
    path('ws/authordel/<int:id>', views.del_author),

    path('ws/publisher', views.get_publisher),
    path('ws/publishers', views.get_publishers),
    path('ws/publishercre', views.create_publisher),
    path('ws/publisherupd', views.update_publisher),
    path('ws/publisherdel/<int:id>', views.del_publisher),

    path('ws/book', views.get_book),
    path('ws/books', views.get_books),
    path('ws/bookcre', views.create_book),
    path('ws/bookupd', views.update_book),
    path('ws/bookdel/<int:id>', views.del_book),
]
