from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_name', 'user_email')

    search_fields = ('title', 'user_name', 'user_email', 'message')
