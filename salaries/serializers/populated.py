from .common import SalarySerializer
from employers.serializers.common import EmployerSerializer

class PopulatedSalarySerializer(SalarySerializer):

    employers = EmployerSerializer(many=True)