from django.contrib import admin

from AppCoder.models import Familiares

# Register your models here.
class FamiliaresAdmin(admin.ModelAdmin):
        
        list_display = ("nombre","apellido","fechaDeNacimiento","email")
        
admin.site.register(Familiares,FamiliaresAdmin)

# admin, admin -> python manage.py createsuperuser