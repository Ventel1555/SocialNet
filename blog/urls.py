from django.urls import path, re_path
from . import views

urlpatterns = [
    path('posts/<slug:slug>/',views.post_detail, name='post_detail'),
    path('',views.post_list, name='post_list'),
    path('posts/new/', views.post_new, name='post_new'),
    path('posts/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
]
