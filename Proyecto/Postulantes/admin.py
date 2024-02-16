from django.contrib import admin

# Register your models here.

from .models import Postulants , StateChange

admin.site.register(Postulants)
admin.site.register(StateChange)
