from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.common import SectorSerializer
from .serializers.populated import PopulatedSectorSerializer

from .models import Sector

class SectorListview(APIView):
    def get(self, _request):
      sectors = Sector.objects.all() 
      serialized_sectors = SectorSerializer(sectors, many=True)
      return Response(serialized_sectors.data, status=status.HTTP_200_OK)
    
class SectorDetailView(APIView):
    def get(self, _request, pk):
      sector = Sector.objects.get(pk=pk)
      serialized_sector = PopulatedSectorSerializer(sector)
      return Response(serialized_sector.data, status=status.HTTP_200_OK)