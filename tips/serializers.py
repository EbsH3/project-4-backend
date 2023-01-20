from rest_framework import serializers
from .models import Tips

from sectors.serializers.common import SectorSerializer

class TipsSerializer(serializers.ModelSerializer):
    class Meta:
      model = Tips
      fields = '__all__'
      
class PopulatedTipsSerializer(TipsSerializer):
  sectors = SectorSerializer(many=True)