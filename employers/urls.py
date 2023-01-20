from django.urls import path
from .views import EmployerDetailView, EmployerListView, EmployerSearchView

urlpatterns = [
  path('', EmployerListView.as_view()),
  path('<int:pk>/', EmployerDetailView.as_view()),
  path('search/', EmployerSearchView.as_view()),
]