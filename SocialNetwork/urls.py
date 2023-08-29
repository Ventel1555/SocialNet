from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('account.urls')),
    path('', include("blog.urls")),
    path('account/', include('django.contrib.auth.urls')),
]
