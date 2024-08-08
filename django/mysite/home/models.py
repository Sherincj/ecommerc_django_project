from django.db import models

# Create your models here.

class item(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=200)
    price=models.IntegerField()
    features=models.CharField(max_length=100)
    



    def __str__(self):
        return str(self.id)+':'+(self.name)