from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
# from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Tips
from .serializers import TipsSerializer, PopulatedTipsSerializer

class TipsListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
    def get(self, _request):
      tip = Tips.objects.all()
      serialized_tip = TipsSerializer(tip, many=True)
      return Response(serialized_tip.data, status=status.HTTP_200_OK)
    
class TipsDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
    def get_tips(self, pk):
      try:
        return Tips.objects.get(pk=pk)
      except Tips.DoesNotExist:
        raise NotFound(detail="Error - Not Found!")
      
    def get(self, _request, pk):
      tips = self.get_tips(pk=pk)
      serialized_tips = PopulatedTipsSerializer(tips)
      return Response(serialized_tips.data, status=status.HTTP_200_OK)
    
    # def put(self, request, pk):
    #   tips_to_edit = self.get_tips(pk=pk)
    #   updated_tips = TipsSerializer(tips_to_edit, data=request.data)
    #   try:
    #     updated_tips.is_valid()
    #     updated_tips.save()
    #     return Response(updated_tips.data, status=status.HTTP_202_ACCEPTED)
    #   except AssertionError as e:
    #     return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      
    #   except:
    #     return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      
    def delete(self, _request, pk):
      tips_to_delete = self.get_tips(pk=pk)
      tips_to_delete.delete
      return Response(status=status.HTTP_204_NO_CONTENT)
      