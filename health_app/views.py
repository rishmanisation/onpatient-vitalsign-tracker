# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Patient, HeartRate, SystolicBloodPressure, DiastolicBloodPressure, Weight, BMI
from main_functions import load_patient_information, load_vitals
from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.http import HttpResponse
from social_django.models import UserSocialAuth

# Create your views here.
def index(request):
    load_patient_information()
    patients = Patient.objects.order_by('-id')
    patient = patients[0]
    context = {
        'patient': patient
    }
    return render(request, 'health_app/index.html', context)

def patient(request):
    load_vitals()
    patients = Patient.objects.order_by('-id')
    contacts = patients[0].patient_contact.split(",") 
    context = {
        'patients': patients,
        'contacts': contacts
    }
    return render(request,'health_app/patient.html',context)

def heartrate(request):
    heart_rate = HeartRate.objects.order_by('-timestamp')
    context = {
        'heart_rate': heart_rate
    }
    return render(request,'health_app/hr.html',context)

def bloodpressure(request):
    sys_bp = SystolicBloodPressure.objects.order_by('-timestamp')
    dia_bp = DiastolicBloodPressure.objects.order_by('-timestamp')
    blood_pressure = []
    
    for i in range(len(sys_bp)):
        blood_pressure.append(str(sys_bp[i].patient_sbp)+'/'+str(dia_bp[i].patient_dbp)+' : '+sys_bp[i].status+' ;'+dia_bp[i].status)
    
    context = {
        'blood_pressure': blood_pressure,
    }
    return render(request,'health_app/bp.html',context)

def bodyweight(request):
    weight = Weight.objects.order_by('-timestamp')
    context = {
        'weight': weight 
    }
    return render(request,'health_app/weight.html',context)

def bodymassindex(request):
    body_mass_index = BMI.objects.order_by('-timestamp')
    context = {
        'body_mass_index': body_mass_index
    }
    return render(request,'health_app/bmi.html',context)