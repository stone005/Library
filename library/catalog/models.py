from django.db import models
from django.urls import reverse
import uuid


class Genere(models.Model):
    """
    Rappresenta il genere del Libro
    """

    descr = models.CharField(
        max_length=200,
        help_text='Inserisci il genere (es. Avventura, Fantascienza, etc.',
        verbose_name='Genere',
    )

    def __str__(self):
        return self.descr


class Book(models.Model):

    titolo = models.CharField(max_length=200, default='', verbose_name='Titolo')
    autore = models.ForeignKey('Autore', on_delete=models.SET_NULL, null=True, verbose_name='Autore')
    # on_delete=models.SET_NULL fa in modo che venga messo Null nel libro in caso l'autore associato venga cancellato

    trama = models.TextField(max_length=1000, help_text='Inserisci la trama', verbose_name='Trama', null=True)
    isbn = models.CharField('ISBN',
                            max_length=13,
                            help_text='13 caratteri <a href="https://www.isbn-international.org/content/what-isbn">Numero ISBN</a>')
    genere = models.ManyToManyField(Genere, help_text='Seleziona il genere', null=True)

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse('book-detail',args=[str(self.id)])


class BookInstance(models.Model):
    """Rappresenta una spacifica copia di quel libro (che potrebbe essere prestato, noleggiato etc. """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID unico per questo particolare libro su tutta la biblioteca')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    rientro = models.DateField(null=True, blank=True)
    Stato_prestito = (
        (1, 'Riparazione'),
        (2, 'In prestito'),
        (3, 'Disponibile'),
        (4, 'Riservato'),
    )
    stato = models.IntegerField(max_length=1, choices=Stato_prestito, default=1, help_text='Disponibilità del libro')

    class Meta:
        ordering = ["rientro"]

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.book.titolo)
        # return f'{self.id} ({self.book.titolo})'


class Autore(models.Model):

    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    nato = models.DateTimeField(null=True, blank=True)
    morto = models.DateTimeField('Morto',null=True, blank=True)

    class Meta:
        ordering = ["cognome","nome"]

    def get_absolute_url(self):
        return reverse('author-details', args=[str(self.id)])

    def __str__(self):
        return '{0},{0}'.format(self.cognome, self.nome)
