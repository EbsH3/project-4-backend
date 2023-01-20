from django.urls import path
from .views import VacancyListView, VacancyDetailView

urlpatterns = [
  path('', VacancyListView.as_view()),
  path('<int:pk>/', VacancyDetailView.as_view())
]