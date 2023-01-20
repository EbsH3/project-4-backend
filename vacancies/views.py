from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from django.db import IntegrityError

from .models import Vacancy
from .serializers import VacancySerializer

class VacancyListView(APIView):

    def get(self, _request):
      vacancies = Vacancy.objects.all()
      serialized_products = VacancySerializer(vacancies, many=True)
      return Response(serialized_products.data, status=status.HTTP_200_OK)
    
    def post(self, request):
      vacancy_to_add = VacancySerializer(data=request.data)
      try:
        vacancy_to_add.is_valid()
        vacancy_to_add.save()
        return Response(vacancy_to_add.data, status=status.HTTP_201_CREATED)
      except IntegrityError as err:
        res = {
          "detail": str(err)
        }
        return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      except AssertionError as err:
          return Response({"detail": str(err) }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      except:
          return Response({"detail": "Unprocessable Entity" }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class VacancyDetailView(APIView):
    def get_vacancy(self, pk):
        try:
            return Vacancy.objects.get(pk=pk)
        except Vacancy.DoesNotExist:
            raise NotFound(detail="Error - that vacancy does not exist!")
          
          
    def get(self, _request, pk):
        vacancy = self.get_vacancy(pk=pk)
        serialized_vacancy = VacancySerializer(vacancy)
        return Response(serialized_vacancy.data, status=status.HTTP_200_OK)   
    
    def put(self, request, pk):
        vacancy_to_edit = self.get_vacancy(pk=pk)
        updated_vacancy = VacancySerializer(vacancy_to_edit, data=request.data)
        try:
          updated_vacancy.is_valid()
          updated_vacancy.save()
          return Response(updated_vacancy.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as err:
          return Response({"detail": str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
          res = {
            "detail": "Unprocessable Entity"
          }
          return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def delete(self, _request, pk):
        vacancy_to_delete = self.get_vacancy(pk=pk)
        vacancy_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
