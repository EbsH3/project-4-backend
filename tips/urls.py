from django.urls import path
from .views import TipsListView, TipsDetailView

urlpatterns = [
  path('', TipsListView.as_view()),
  path('', TipsDetailView.as_view())
]