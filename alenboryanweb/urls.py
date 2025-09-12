from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),        # главная
    path('about/', include('apps.about.urls')), # about
    path('projects/', include('apps.projects.urls')), # projects
    path('contact/', include('apps.contact.urls')),   # contact
]
