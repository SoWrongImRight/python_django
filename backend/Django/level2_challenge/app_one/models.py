from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    mail = models.EmailField(max_length=75, unique=True)

    def __str__(self):
        return self.fname
