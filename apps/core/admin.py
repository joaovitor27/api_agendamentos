from django.contrib import admin
from .models import Reservation, Workstations
# Register your models here.

admin.site.register(Reservation)
admin.site.register(Workstations)
