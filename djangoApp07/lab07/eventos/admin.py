# Register your models here.

from django.contrib import admin
from .models import Evento, RegistroEvento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'organizador')
    search_fields = ('nombre', 'organizador__username')
    list_filter = ('fecha',)

@admin.register(RegistroEvento)
class RegistroEventoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'evento', 'fecha_registro')
    search_fields = ('usuario__username', 'evento__nombre')
    list_filter = ('fecha_registro',)