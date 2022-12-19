from django.db import models


class Data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    status=models.CharField(max_length=50)


    def __str__(self):
        return self.first_name + " "+self.last_name