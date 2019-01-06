from django.conf import settings
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_auth.registration.views import SocialLoginView


from bitsplit.corpus import models
from . import serializers


class ListBits(APIView):
    def get(self, request):
        bits = models.Bit.objects.all()
        serializer = serializers.BitSerializer(bits, many=True)
        return Response(serializer.data)

class ListBitsplits(APIView):
    def get(self, request):
        bitsets = models.BitSet.objects.all()
        serializer = serializers.BitSetSerializer(bitsets, many=True)
        return Response(serializer.data)


class GoogleLogin(SocialLoginView):
    authentication_classes = (JSONWebTokenAuthentication,)
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.CALLBACK_URL
    client_class = OAuth2Client
