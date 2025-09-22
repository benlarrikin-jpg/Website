from django.urls import path
from cars.views import house

urlpatterns = [
    path('jump/', house , name='door'),
]
