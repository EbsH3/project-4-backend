from django.db import models

class Salary(models.Model):
  title = models.CharField(max_length=50)
  level_of_experience = models.CharField(max_length=50)
  salary_benchmark = models.CharField(max_length=200)
  sector = models.ManyToManyField('sectors.Sector', related_name="salaries")
  
  
  def __str__(self):
    return f"{self.title} - {self.sector}"