from django.db import models

# Create your models here.

class PersonalInformation(models.Model):
    SEQN = models.AutoField(primary_key=True)
    Name = models.CharField(max_length = 250)
    Gender = models.IntegerField(max_length=10)
    Age = models.IntegerField()
    Race = models.IntegerField(max_length=30, blank=True, null=True)
    Height = models.FloatField(blank=True, null=True)
    Weight = models.FloatField()
    Bmi = models.FloatField()
    Email = models.EmailField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)

class LabReports(models.Model):
    SEQN = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE)
    Diabetes_Status = models.IntegerField(max_length=30, blank=True, null=True)
    HbA1c = models.FloatField(blank=True, null=True)
    Glucose = models.FloatField(blank=True, null=True)
    cholesterol = models.FloatField()
    Triglycerides = models.FloatField()
    Blood_Pressure_Systolic = models.FloatField(blank=True, null=True)
    Blood_Pressure_Diastolic = models.FloatField(blank=True, null=True)

class Lifestyle(models.Model):
    SEQN = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE)
    SmokingStatus = models.IntegerField(max_length=10, blank=True, null=True)
    AlcoholConsumption = models.IntegerField(max_length=10, blank=True, null=True)
    ActivityLevel = models.FloatField()
    SleepDuration = models.IntegerField(blank=True, null=True)

class MedicalHistory(models.Model):
    SEQN = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE)
    DiabetesPedigree = models.IntegerField(max_length=10, blank=True, null=True)
    PCOD = models.IntegerField(max_length=10, blank=True, null=True)
    Pregnancy = models.IntegerField(max_length=10, blank=True, null=True)


class demographic_data(models.Model):
    region = models.CharField(max_length = 255)
    country = models.CharField(max_length = 255)
    year_2000 = models.FloatField(default = 0)
    year_2011 = models.FloatField(default = 0)
    year_2021 = models.FloatField(default = 0)
    year_2030 = models.FloatField(default = 0)
    year_2045 = models.FloatField(default = 0)


