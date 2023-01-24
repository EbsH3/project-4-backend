from django.db import models

class Vacancy(models.Model):
  title = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  employer = models.ManyToManyField('employers.Employer', related_name="vacancies")
  salary = models.CharField(max_length=50)
  url = models.CharField(max_length=700)
  
  def __str__(self):
    return f"{self.title} - {self.location}" 