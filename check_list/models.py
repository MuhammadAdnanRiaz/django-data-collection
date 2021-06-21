from django.db import models
from images.models import Images
# Create your models here.

class Checklist(models.Model):
    json = models.JSONField()
    x = models.IntegerField(max_length=10000)
    y = models.IntegerField(max_length=10000)
    image = models.ForeignKey(Images,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.json["question"]