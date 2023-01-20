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
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
      request.data["owner"] = request.user.id
      feedback_to_add = FeedbackSerializer(data=request.data)
      try:
          feedback_to_add.is_valid()
          feedback_to_add.save()
          return Response(feedback_to_add.data, status=status.HTTP_201_CREATED)
      except IntegrityError as err:
          return Response ({"detail": str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      except AssertionError as err:
          return Response({"detail": str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      except:
          return Response("Unprocessable Entity", status=status.HTTP_422_UNPROCESSABLE_ENTITY) 
        
class FeedbackDetailView(APIView):
    def delete(self, request, pk):
        try:
            delete_feedback = Feedback.objects.get(pk=pk)
            if delete_feedback.owner != request.user:
                raise PermissionDenied()
            delete_feedback.delete() 
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Feedback.DoesNotExist:
            raise NotFound(detail="Error - Not Found!")