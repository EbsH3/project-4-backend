from django.urls import path
from .views import SalaryListView, SalaryDetailView

urlpatterns = [
  path('', SalaryListView.as_view()),
  path('<int:pk>/', SalaryDetailView.as_view())
] 