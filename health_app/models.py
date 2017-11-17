# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Patient(models.Model):
    # Patient id
    id = models.CharField(max_length=140, primary_key=True)
    
    # Patient name
    patient_name = models.CharField(max_length=140)

    # Patient gender
    patient_sex = models.CharField(max_length=140)

    # Patient birth date
    patient_dob = models.DateField()
    
    # Patient contact
    patient_contact = models.CharField(max_length=1000, null=True)

    def __unicode__(self):
        return self.patient_name

class HeartRate(models.Model):

    # Patient heart rate
    patient_hr = models.FloatField(null=True)
    timestamp = models.DateTimeField(primary_key=True)
    status = models.CharField(max_length=140)

    def __unicode__(self):
        return str(self.patient_hr)

class SystolicBloodPressure(models.Model):

    # Patient heart rate
    patient_sbp = models.FloatField(null=True)
    timestamp = models.DateTimeField(primary_key=True)
    status = models.CharField(max_length=140)

    def __unicode__(self):
        return str(self.patient_sbp)

class DiastolicBloodPressure(models.Model):

    patient_dbp = models.FloatField(null=True)
    timestamp = models.DateTimeField(primary_key=True)
    status = models.CharField(max_length=140)

    def __unicode__(self):
        return str(self.patient_dbp)

class Weight(models.Model):

    # Patient heart rate
    patient_weight = models.FloatField(null=True)
    timestamp = models.DateTimeField(primary_key=True)

    def __unicode__(self):
        return str(self.patient_weight)

class BMI(models.Model):

    # Patient heart rate
    patient_bmi = models.FloatField(null=True)
    timestamp = models.DateTimeField(primary_key=True)
    status = models.CharField(max_length=140)

    def __unicode__(self):
        return str(self.patient_bmi) 


