from django.db import models

# Create your models here.

class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=60)
    salary=models.IntegerField()

    def __str__(self):
        return self.name


