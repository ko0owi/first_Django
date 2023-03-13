from django.db import models

class Estate (models.Model):
    ename = models.CharField(max_length=32)

    def __str__(self):
        return self.ename



class Task (models.Model):
    name = models.CharField(max_length= 64)
    adress = models.CharField(max_length= 32)
    presence = models.BooleanField
    added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name






