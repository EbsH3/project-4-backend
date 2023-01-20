from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers.common import EmployerSerializer
from .serializers.populated import PopulatedEmployerSerializer
from .models import Employer


class EmployerListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
    def get(self, _request):
      employers = Employer.objects.all()
      serialized_employers = EmployerSerializer(employers, many=True)
      return Response(serialized_employers.data, status=status.HTTP_200_OK)

class EmployerDetailView(APIView):
    def get(self, _request, pk):
      employer = Employer.objects.get(pk=pk)
      serialized_employer = PopulatedEmployerSerializer(employer)
      return Response(serialized_employer.data, status=status.HTTP_200_OK)
    
    def delete(self, _request, pk):
      employer_to_delete = self.get_employer(pk=pk)
      employer_to_delete.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
      employer_to_edit = self.get_employer(pk=pk)
      updated_employer = EmployerSerializer(employer_to_edit, data=request.data)
      try:
          updated_employer.is_valid()
          updated_employer.save()
          return Response(updated_employer.data, status=status.HTTP_202_ACCEPTED)
      except AssertionError as err:
        return Response({"detail": str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      except:
          res = {
              "detail": "Unprocessable Entity"
          }
          return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class EmployerSearchView(APIView):
    def get(self, request):
        search_query = request.GET.get('search')
        print("Searching for", search_query)
        results = Employer.objects.filter(title__icontains=search_query)
        serialized_results = EmployerSerializer(results, many=True)
        return Response(serialized_results.data)