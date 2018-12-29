from django.urls import path

from .views import ListBitsplits


urlpatterns = [
    path('', ListBitsplits.as_view(), name='bitsplit_list'),
]
