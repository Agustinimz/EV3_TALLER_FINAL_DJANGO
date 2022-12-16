from django.contrib import admin
from serialApp.models import Reserva

# Register your models here.
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['institucion', 'id']

admin.site.register(Reserva, ReservaAdmin)