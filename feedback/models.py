from django.db import models

class Feedback(models.Model):
  text = models.TextField(max_length=300)
  employer = models.ManyToManyField('employers.Employer', related_name="feedback")
  owner = models.ForeignKey("jwt_auth.User", related_name="feedback", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  