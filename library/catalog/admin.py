from django.contrib import admin
from .models import Autore, Genere, Language, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Autore)
#admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genere)


class BookInline(admin.TabularInline):
    model = Book


class AutoreAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cognome', 'nato', 'morto')
    fields = ['nome', 'cognome', ('nato', 'morto')]
    inlines = [BookInline]


admin.site.register(Autore, AutoreAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'autore', 'display_genere')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('stato', 'rientro')
    list_display = ('book', 'stato', 'rientro', 'id')
    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Disponibilità', {'fields': ('stato', 'rientro')}),
    )

