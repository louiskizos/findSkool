from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Skool(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='assets/')
    designationEcole = models.CharField(max_length=255)
    arreteMin = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    typesEcole = models.CharField(max_length=50)
    promoteur = models.CharField(max_length=255)
    biographie = models.TextField()

    def __str__(self):
        return self.designationEcole

class Degree(models.Model):
    skool = models.ForeignKey(Skool, related_name='degrees', on_delete=models.CASCADE)
    designation = models.CharField(max_length=150)

    def __str__(self):
        return self.designation

class Option(models.Model):
    degree = models.ForeignKey(Degree, related_name='options', on_delete=models.CASCADE)
    option = models.CharField(max_length=150)
    classe = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.option} - {self.classe}"
