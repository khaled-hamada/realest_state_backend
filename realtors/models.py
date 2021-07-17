from django.db import models
from datetime import datetime
from django.utils.timezone  import now
# Create your models here.


class Realtor(models.Model):
    name = models.CharField(max_length=264)
    photo = models.ImageField(upload_to="realtos_photos/%Y/%m%d")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=now , blank=True)


    def __str__(self):
        return self.name
    

    
