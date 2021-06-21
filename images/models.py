from django.db import models

# Create your models here.

class Images(models.Model):
    file = models.ImageField(upload_to='uploads/')
    sequence = models.IntegerField(max_length=1000)

    def __str__(self):
        return self.file.name