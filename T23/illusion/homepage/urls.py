from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', include('homepage.urls')),
    path('tourdates/', include('tourdates.urls')),
    path('contact/', include('contact.urls')),
]