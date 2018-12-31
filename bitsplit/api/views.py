from rest_framework.views import APIView
from rest_framework.response import Response

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
