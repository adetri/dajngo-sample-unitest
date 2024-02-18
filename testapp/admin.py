from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',
                    'date_of_birth', 'created_at', 'updated_at')
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['date_of_birth']
