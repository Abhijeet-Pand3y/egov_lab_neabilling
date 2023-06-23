from django.db import models

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.name