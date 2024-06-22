from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


Gender_choice=(('Male','Male'),
               ('Female','Female'))

class patients(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='patient')
    Name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=10)
    age=models.IntegerField()
    Address = models.CharField(max_length=255)
    Location = models.CharField(max_length=100)
    Email = models.EmailField()
    Gender = models.CharField(max_length=100,choices=Gender_choice)

    def __str__(self):
        return self.Name



class Doctors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctor')

    Name = models.CharField(max_length=255)
    Speciality =models.CharField(max_length=100)
    Area_of_expertise =models.CharField(max_length=100)
    Phone = models.CharField(max_length=10)
    Email = models.EmailField()
    Document = models.ImageField(upload_to= 'doctor')
    Approve_status = models.IntegerField(default=0)

    def __str__(self):
        return self.Name




