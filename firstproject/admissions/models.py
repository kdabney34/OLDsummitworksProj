from django.db import models

# Create your models here.

class Admission(models.Model):
    personName = models.CharField(max_length=40)
    movieName = models.CharField(max_length=40)

    def __str__(self):
        return str(self.personName) + "  --watched--  " + str(self.movieName)


