from django.db import models

# Create your models here.
class StudentsModel(models.Model):
    name=models.CharField(max_length=50)
    roll_number=models.IntegerField()
    email=models.EmailField()
    department=models.CharField(max_length=30)
    dob=models.DateField()
    

    def __str__(self):
        return self.name


class TempModel(models.Model):   # deleted students
    name = models.CharField(max_length=50)
    roll_number = models.IntegerField()
    email = models.EmailField()
    department = models.CharField(max_length=30)
    dob = models.DateField()

    def __str__(self):
        return self.name