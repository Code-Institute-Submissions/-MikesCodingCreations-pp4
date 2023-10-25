from django.db import models

# Create your models here.


class Reservation(models.Model):
    full_Name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.full_Name
