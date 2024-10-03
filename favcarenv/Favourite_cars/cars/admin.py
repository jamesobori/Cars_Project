from django.contrib import admin
from .models import Cars,Contact 


# Register your models here.
class CarsAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'type', 'speed')
admin.site.register(Cars, CarsAdmin)
admin.site.register(Contact)