from django.contrib import admin
from pzwebapp.models import Language, Korisnik, Exchange, LanguageExchange

admin.site.register(Language)
admin.site.register(Korisnik)
admin.site.register(Exchange)
admin.site.register(LanguageExchange)