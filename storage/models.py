from django.db import models

class Storage(models.Model):
    url = models.URLField()
    data = models.TextField()

    def __str__(self):
        return self.url
