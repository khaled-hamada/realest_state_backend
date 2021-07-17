from django.db import models
from django.utils.timezone import now


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.email
