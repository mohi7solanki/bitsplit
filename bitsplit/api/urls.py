from django.urls import path

from .views import ListBitsplits, ListBits


urlpatterns = [
    path('bits', ListBits.as_view(), name='bits_list'),
    path('bitsplits', ListBitsplits.as_view(), name='bitsplit_list'),
]
