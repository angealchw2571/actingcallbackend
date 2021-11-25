from django.db import models
from profiles.models import Profiles

# Create your models here.

class Castcall(models.Model):
    type = models.CharField(max_length=50)
    platform = models.CharField(max_length=30)
    period = models.IntegerField(default=0)
    role = models.CharField(max_length=50)
    details = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    company = models.CharField(max_length=50)
    remuneration = models.IntegerField(default=0)
    loadingScale = models.CharField(max_length=50)
    contract = models.BooleanField(default=False)
    postedBy = models.ForeignKey(Profiles, on_delete=models.CASCADE, related_name="casts")

    def __str__(self):
        return self.type


