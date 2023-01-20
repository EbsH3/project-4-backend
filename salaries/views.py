from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.common import SalarySerializer
from .serializers.populated import PopulatedSalarySerializer

from .models import Salary

class SalaryListView(APIView):
  def get(self, _request):
    salaries = Salary.objects.all();
    serialized_salaries = SalarySerializer(salaries, many=True)
    return Response(serialized_salaries.data, status=status.HTTP_200_OK)
  
class SalaryDetailView(APIView):
  def get(self, _request, pk):
    salary = Salary.objects.get(pk=pk)
    serialized_salary = PopulatedSalarySerializer(salary)
    return Response(serialized_salary.data, status=status.HTTP_200_OK)