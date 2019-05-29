from django.contrib import admin
from .models import Employees

# admin.site.register(Employees)

@admin.register(Employees)
class ListEmployee(admin.ModelAdmin):
    list_display = ('name', 'email','departament')
    list_filter = ('name',)
    search_fields = ('name',)