from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)

    def __str__(self):
        return str(self.name) + "  --watched--  " + str(self.description)


