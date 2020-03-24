from django.db import models


class Retailer(models.Model):
    """ Model class for Retailer"""
    name = models.CharField(max_length=50)
    url = models.URLField()
    
    def __str__(self):
        return self.name
