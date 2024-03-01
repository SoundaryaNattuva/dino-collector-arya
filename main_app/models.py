from django.db import models
from django.urls import reverse
from datetime import date

# a tuple of 2-tuple. first item - value stored in DB. second item - human-friendly display value
SHOTS = (
  ('F', 'Flu'),
  ('P', 'Parvovirus'),
  ('R', 'Rotavirus'),
  ('T', 'Tetanus'),
  ('M', 'Measles'),
)

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
  
  def get_absolute_url(self):
    return reverse('dino-detail', kwargs={'dino_id': self.id})
  
  def vaccine_for_today(self):
    return self.vaccine_set.filter(date=date.today()).count() <= 2
  
class Vaccine(models.Model):
  date = models.DateField('Vaccine Administration Date')
  shot = models.CharField('Vaccine Administered',
    max_length=1,
    choices=SHOTS,
    default=SHOTS[0][0]
  )
  # Create a dino_id column in the database
  dino = models.ForeignKey(Dino, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.get_shot_display()} on {self.date}"
  
  class Meta: 
    ordering = ['-date']

# Add the Toy model
class Milestone(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('milsetone-detail', kwargs={'pk': self.id})