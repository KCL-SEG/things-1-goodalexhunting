from django.db import models
from django.db.models import MinValueValidator
from django.db.models import MaxValueValidator

# Create your models here.
class Thing(django.db.models.Model):
    name = models.CharField(max_length = 30, unique=True)
    description = models.TextField(max_length = 120,blank = True, unique = False)
    quantity = models.IntegerField(validators = [
        MinValueValidator(0,message='Cannot be less than 0'),
        MinValueValidator(100,message='Cannot be more than 100')]
    # ,
    # validators= [RegexValidator(
    #     regex =r'^@\w{3,}$',
    #     message ='Username must consist of @ symbol followed by atleast 3 alpha numericals'
    # )]
    )
