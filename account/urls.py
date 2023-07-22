from django.urls import path
from . import views


urlpatterns = [
    # login / logout urls
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
]