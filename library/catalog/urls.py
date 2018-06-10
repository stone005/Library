from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookViewList.as_view(), name='books'),
    path('authors/', views.AuthorViewList.as_view(), name='authors'),
    path('book/(?P<pk>\d+)', views.BookDetailView.as_view(), name='book-detail'),
    path('autore/(?P<pk>\d+)', views.AutoreDetailView.as_view(), name='autore-detail'),
    # pagine di autenticazione django, è sufficiente creare i file html sotto templates\registration
    path('accounts/', include('django.contrib.auth.urls')),
]