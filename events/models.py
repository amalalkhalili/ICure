from django.contrib.auth.models import User
from django.db import models

class Doctors(models.Model):
    Cit_Id = models.FloatField(max_length=10)
    Specialization_Id = models.FloatField(max_length=10)
    Doctor_Id = models.AutoField(primary_key=True)
    Doctor_Name = models.CharField(max_length=255)
    Doctor_Address = models.CharField(max_length=255)

    class Meta:
        db_table = 'Doctor'


class City(models.Model):
    City_Id = models.AutoField(primary_key=True)
    City_Name = models.CharField(max_length=255)
    class Meta:
         db_table='City'


class Specialization(models.Model):
    Specialization_Id = models.IntegerField(primary_key=True)
    Specialization = models.CharField(max_length=255)

    class Meta:
        db_table = 'Specialization'

class Hospital(models.Model):
    City_Id = models.IntegerField
    Area_Id = models.IntegerField
    Hospital_Id = models.AutoField(primary_key=True)
    Hospital_Name = models.CharField(max_length=255)
    Hospital_Address = models.CharField(max_length=255)

    class Meta:
        db_table = 'Hospital'

class Area(models.Model):
    City_Id = models.ForeignKey('City', on_delete=models.CASCADE)
    Area_Id = models.AutoField(primary_key=True)
    Area_Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'Area'




class Symptoms(models.Model):
    Symptoms = models.CharField(max_length=255)

    class Meta:
        db_table = 'Symptoms'

class Disease(models.Model):
    Disease_Id = models.FloatField(primary_key=True)
    Disease_Name = models.CharField(max_length=255)
    class Meta:
        db_table = 'Disease'

class FinalResult(models.Model):
    Disease_ID = models.FloatField(primary_key=True)
    Disease = models.CharField(max_length=255)
    Specialization = models.CharField(max_length=255)
    Symptoms= models.CharField(max_length=255)
    Medications= models.CharField(max_length=255)

    class Meta:
        db_table = 'Final_Full_Data'


class MedicalHistory(models.Model):
    CHRONIC_CHOICES = [
        (1, 'Yes'),
        (0, 'No')
    ]
    ALLERGIC_CHOICES = [
        (1, 'Yes'),
        (0, 'No')
    ]
    MEDICATION_CHOICES = [
        (1, 'Yes'),
        (0, 'No')
    ]

    print("In MedicalHistory")
    #user_id = models.ForeignKey(ICureUser, on_delete=models.CASCADE)
    is_chronic_disease = models.IntegerField(choices=CHRONIC_CHOICES, default=0)
    disease_type = models.TextField(default='none', blank=True, null=True)
    is_on_medication = models.IntegerField(choices=ALLERGIC_CHOICES, default=0)
    medication_name = models.CharField(max_length=100, blank=True, null=True)
    is_allergic = models.IntegerField(choices=MEDICATION_CHOICES, default=0)
    allergy = models.CharField(default='none',max_length=200, blank=True, null=True)

    print("Out ICureUser")


    def __str__(self):
        return self.is_chronic_disease
