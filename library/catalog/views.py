from django.shortcuts import render
from .models import Book, Autore, BookInstance, Genere, Language
from django.views import generic
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """
    View per Homepage del sito
    """
    # Genero il conteggio degli oggetti

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Disponibili (stato = 3)
    num_instances_disp = BookInstance.objects.filter(stato__exact=3).count()

    num_generi = Genere.objects.count()
    num_autori = Autore.objects.count()

    # Libri che contengono la parola 'montalbano'
    num_libri_mont = Book.objects.filter(titolo__icontains='montalbano').count()

    # Numero di visite memorizzate in una Session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Inviare il template index.html con i dati memorizzati nella session
    return render(
        request,
        'index.html',
        context={'num_books': num_books,
                 'num_instances': num_instances,
                 'num_instances_disp': num_instances_disp,
                 'num_autori': num_autori,
                 'num_generi': num_generi,
                 'num_libri_mont': num_libri_mont,
                 'num_visits': num_visits
                 },
    )


class BookViewList(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorViewList(generic.ListView):
    model = Autore


class AutoreDetailView(generic.DetailView):
    model = Autore
