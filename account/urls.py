from django.urls import path
from . import views


urlpatterns = [
    # login / logout urls
    path('post-changes/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]