from .common import SectorSerializer
from salaries.serializers.common import SalarySerializer
from tips.serializers import TipsSerializer

class PopulatedSectorSerializer(SectorSerializer):
    salaries = SalarySerializer
    tips = TipsSerializer