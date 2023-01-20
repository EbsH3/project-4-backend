from django.db import models

class Employer(models.Model):
  employer = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  logo = models.CharField(max_length=700)
  sector = models.ManyToManyField('sectors.Sector', related_name="employers")
  # owner = models.ForeignKey('jwt_auth.User', related_name="employers", on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.employer} - {self.location}"
  