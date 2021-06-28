from django.db import models
from check_list.models import Checklist 
# Create your models here.

class Answers(models.Model):

    answer = models.TextField()
    inspection_type = models.TextField(null=True)
    created_at  = models.DateField(auto_now_add=True)
    updated_at  = models.DateField(auto_now=True)
    question = models.ForeignKey(Checklist,on_delete=models.CASCADE,null=False)
    vehicle = models.IntegerField(default=1)

   