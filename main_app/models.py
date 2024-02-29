from django.db import models

# Create your models here.
class Dino(models.Model):
  name = models.CharField(max_length=100)
  dinosaurType = models.CharField(max_length=100)
  age = models.IntegerField()
  diet = models.CharField(max_length=100)
  length = models.DecimalField(max_digits=5, decimal_places=2)
  height = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return self.name
