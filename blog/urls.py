from django.urls import path, re_path
from . import views

urlpatterns = [
    path('posts/<slug:slug>/',views.post_detail, name='post_detail'),
    path('',views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('posts/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('posts/<slug:slug>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
]
