from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookViewList.as_view(), name='books'),
    url(r'^authors/$', views.AuthorViewList.as_view(), name='authors'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^autore/(?P<pk>\d+)$', views.AutoreDetailView.as_view(), name='autore-detail'),
    url(r'^accounts/$', include('django.contrib.auth.urls')),   # pagina di autenticazione django
]
