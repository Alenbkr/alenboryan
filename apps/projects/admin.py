from django.contrib import admin


from django.contrib import admin


from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ("name", "start_date", "end_date", "technologies_used")  
    search_fields = ("name", "technologies_used")  
    list_filter = ("start_date", "end_date") 

    list_display = ('title', 'name', 'owner', 'start_date', 'created_at')
    search_fields = ('title', 'name', 'description', 'technologies_used')
    list_filter = ('owner', 'start_date', 'created_at')
