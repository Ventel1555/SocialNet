import django.contrib.auth.views
from django.urls import path
from . import views
from django.contrib.auth.views import logout_then_login
# urlpatterns = [
#     # post views
#     path('login/', views.user_login, name='login'),
# ]

urlpatterns = [
    # login / logout urls
    path('', views.dashboard, name='dashboard'),
]