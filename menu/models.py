from django.db import models
from django.utils.text import slugify

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='menu/')
    slug = models.SlugField(blank=True, null=True)

    def __str__(self): 
        return self.name