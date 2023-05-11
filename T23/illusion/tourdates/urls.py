from django.urls import path
from tourdates.views import tourdates

urlpatterns = [
    path('', tourdates, name='tourdates'),
]