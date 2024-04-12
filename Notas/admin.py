from django.contrib import admin
from .models import Tarea
# Register your models here.
@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "estado")