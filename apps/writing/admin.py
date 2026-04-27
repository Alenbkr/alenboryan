from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'start_date', 'created_at')
    search_fields = ('title', 'description', 'technologies_used')
    list_filter = ('owner', 'start_date', 'created_at')
