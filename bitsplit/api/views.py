from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


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
    callback_url = 'http://localhost:8000/accounts/google/login/callback/'
    client_class = OAuth2Client
