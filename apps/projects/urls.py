from django.urls import path

from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]

from .views import ProjectListView, ProjectDetailView, ProjectCreateView
ProjectCreateView
urlpatterns = [
    path('', ProjectListView.as_view(), name='projects'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
     path('create/', ProjectCreateView.as_view(), name='project_create'),
]



