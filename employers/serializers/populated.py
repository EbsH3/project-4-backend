from .common import EmployerSerializer
from vacancies.serializers import VacancySerializer
from feedback.serializers.populated import PopulatedFeedbackSerializer
from sectors.serializers.common import SectorSerializer

class PopulatedEmployerSerializer(EmployerSerializer):
    vacancies = VacancySerializer(many=True)
    feedback = PopulatedFeedbackSerializer(many=True)
    sector = SectorSerializer
