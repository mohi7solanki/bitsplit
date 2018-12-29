from rest_framework.views import APIView
from rest_framework.response import Response

from bitsplit.corpus.models import BitSet
from .serializers import BitSetSerializer


class ListBitsplits(APIView):
    def get(self, request):
        bitsets = BitSet.objects.all()
        serializer = BitSetSerializer(bitsets, many=True)
        return Response(serializer.data)
