from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from django.db import IntegrityError
from .serializers.common import FeedbackSerializer
from .models import Feedback

class FeedbackListView(APIView):
    permission_classes = (IsAuthenticated, )
    
    def post(self, request):
      request.data["owner"] = request.user.id
      feedback_to_add = FeedbackSerializer(data=request.data)
      print(feedback_to_add)
      try:
          feedback_to_add.is_valid()
          feedback_to_add.save()
          return Response(feedback_to_add.data, status=status.HTTP_201_CREATED)
      except IntegrityError as e:
        res = {
          "detail": str(e)
        }
        return Response (res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      except AssertionError as e:
          return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      except:
          return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY) 
        
class FeedbackDetailView(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, _request, pk):
      feedback = Feedback.objects.get(pk=pk)
      serialized_feedback = FeedbackSerializer(feedback)
      return Response(serialized_feedback.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
      try:
        delete_feedback = Feedback.objects.get(pk=pk)
        if delete_feedback.owner != request.user:
          raise PermissionDenied()
        
        delete_feedback.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
      except Feedback.DoesNotExist:
        raise NotFound(detail="Error - Not Found!")
      
    def put(self, request, pk):
        feedback_to_update = Feedback.objects.get(pk=pk)
        if feedback_to_update.owner != request.user:
          raise PermissionDenied()
        
        updated_feedback = FeedbackSerializer(feedback_to_update, data=request.data)
        
        try:
          updated_feedback.is_valid()
          updated_feedback.save()
          return Response(updated_feedback.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
          return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
          return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      