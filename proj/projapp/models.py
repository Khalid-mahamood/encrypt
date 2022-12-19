from django.db import models


# Create your models here.
class encrypt(models.Model):
    Name = models.TextField()

    def __str__(self):
        return self.Name
