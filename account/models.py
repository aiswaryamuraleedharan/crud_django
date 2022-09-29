from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    name=models.CharField(max_length=25)
    # age=models.IntegerField()
    # place=models.CharField(max_length=25)
    mark=models.IntegerField()
    def __str__(self):
        return self.name