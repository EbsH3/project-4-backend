from django.urls import path
from .views import SectorListview, SectorDetailView

urlpatterns = [
  path('', SectorListview.as_view()),
  path('', SectorDetailView.as_view())
]