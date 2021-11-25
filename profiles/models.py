from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Profiles(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    height = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(250)], default=0)
    weight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)], default=0)
    displayPicture = models.CharField(max_length=300)
    language = ArrayField(models.CharField(max_length=50))
    contact = models.CharField(max_length=20)
    personalStatement = models.CharField(max_length=1000)
    hairColor = models.CharField(max_length=20)
    eyeColor = models.CharField(max_length=20)
    accents = ArrayField(models.CharField(max_length=50))
    skills = ArrayField(models.CharField(max_length=50))
    playAgeMin = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)], default=25)
    playAgeMax = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)], default=35)
    links = models.CharField(max_length=500)
    education = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    accountLinked = models.OneToOneField(User, on_delete=models.CASCADE, null=True,related_name="profiles")

    def __str__(self):
        return self.name


