from django.shortcuts import render
from .models import Book, Autore, BookInstance, Genere, Language


def index(request):
    """
    View per Homepage del sito
    """
    # Genero il conteggio degli oggetti

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #Disponibili (stato = 3)

    num_instances_disbonibili = BookInstance.objects.filter(status__exact=3).count()
    num_autori=Autore.objects.count()

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances, 'num_instances_disbonibili': num_instances_disbonibili, 'num_autori': num_autori}
    )
