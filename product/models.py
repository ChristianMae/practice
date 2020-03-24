from django.db import models
from retailer.models import Retailer


class Product(models.Model):
    """ Model class for Product. """
    name = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=True)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name