from django.contrib import admin
from .models import Autore, Genere, Language, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Autore)
#admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genere)


class AutoreAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cognome', 'nato', 'morto')


admin.site.register(Autore, AutoreAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'autore', 'display_genere')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
