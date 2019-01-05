from django.urls import path

from .views import ListBitsplits, ListBits, GoogleLogin


urlpatterns = [
    path('bits/', ListBits.as_view(), name='bits_list'),
    path('bitsplits/', ListBitsplits.as_view(), name='bitsplit_list'),
    path('google/login/', GoogleLogin.as_view(), name='google_login'),
]
