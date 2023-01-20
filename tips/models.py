from django.db import models

class Tips(models.Model):
  name = models.CharField(max_length=50)
  detail = models.TextField(max_length=500)
  sector = models.ManyToManyField('sectors.Sector', related_name="tips")

  def __str__(self):
    return f"{self.name} - {self.sector}"