import api_functions
from .models import Patient, HeartRate, SystolicBloodPressure, DiastolicBloodPressure, Weight, BMI
from social_django.models import UserSocialAuth

def load_patient_information():
    socialonpatient = UserSocialAuth.objects.filter(provider='onpatient')[0]
    patients = api_functions.get_patient(socialonpatient)
    for patient in patients:
        if not Patient.objects.filter(id=str(patient['identifier'])).exists():
            contact = ''
            for com in patient['telecom']:
                contact = contact + com['use'] + ' ' + com['system'] + ": " + com['value'] + ','
            contact = contact[:-1]
            patient_obj = Patient.objects.create(
                id = str(patient['identifier']),
                patient_name = patient['name'][0]['given'][0] + ' ' + patient['name'][0]['family'][0],
                patient_sex = patient['gender'],
                patient_dob = patient['birthDate'],
                patient_contact = contact
            )
            patient_obj.save()

def split_timestamp(timestamp):
    ts_split = timestamp.split('T')
    return ts_split[0] + ' ' + ts_split[1]

def load_vitals():
    socialonpatient = UserSocialAuth.objects.filter(provider='onpatient')[0]
    observations = api_functions.get_observations(socialonpatient)
    for observation in observations:
        #if observation['category']['text'] == 'Vital Signs':
        if observation['code']['text'] == 'Body pulse':
            if not HeartRate.objects.filter(timestamp=split_timestamp(observation['effectiveDateTime'])).exists():
                heart_rate = observation['valueQuantity']['value']
                ts = split_timestamp(observation['effectiveDateTime'])
                if heart_rate >= 80:
                    msg = 'High heart rate'
                elif heart_rate < 60:
                    msg = 'Low heart rate'
                else:
                    msg = 'Normal heart rate'
                hr_obj = HeartRate.objects.create(
                    patient_hr = heart_rate,
                    timestamp = ts,
                    status = msg
                )
                hr_obj.save()
            else:
                hr_obj = HeartRate.objects.filter(timestamp=split_timestamp(observation['effectiveDateTime']))[0]
        elif observation['code']['text'] == 'Body weight':
            if not Weight.objects.filter(timestamp=split_timestamp(observation['effectiveDateTime'])).exists():
                weight = observation['valueQuantity']['value']
                ts = split_timestamp(observation['effectiveDateTime'])
                wt_obj = Weight.objects.create(
                    patient_weight = weight,
                    timestamp = ts
                )
                wt_obj.save()
            else:
                wt_obj = Weight.objects.filter(timestamp=split_timestamp(observation['effectiveDateTime']))[0]
        elif observation['code']['text'] == 'Systolic blood pressure':
            if not SystolicBloodPressure.objects.filter(timestamp=split_timestamp(observation['effectiveDateTime'])).exists():
                sbp = observation['valueQuantity']['value']
                ts = split_timestamp(observation['effectiveDateTime'])
                if sbp >= 130:
                    msg = 'High systolic BP'
                elif sbp < 90:
                    msg = 'Low systolic BP'
                else:
                    msg = 'Systolic BP is OK'
                sbp_obj = SystolicBloodPressure.objects.create(
                    patient_sbp = sbp,
                    timestamp = ts,
                    status = msg
                )
                sbp_obj.save()
            else:
                sbp_obj = SystolicBloodPressure.objects.filter(timestamp=split_timestamp(observation['effectiveDateTime']))[0]
        elif observation['code']['text'] == 'Diastolic blood pressure':
            if not DiastolicBloodPressure.objects.filter(timestamp=split_timestamp(observation['effectiveDateTime'])).exists():
                dbp = observation['valueQuantity']['value']
                ts = split_timestamp(observation['effectiveDateTime'])
                if dbp >= 90:
                    msg = 'High diastolic BP'
                elif dbp < 60:
                    msg = 'Low diastolic BP'
                else:
                    msg = 'Diastolic BP is OK'
                dbp_obj = DiastolicBloodPressure.objects.create(
                    patient_dbp = dbp,
                    timestamp = ts,
                    status = msg
                )
                dbp_obj.save()         
            else:
                dbp_obj = DiastolicBloodPressure.objects.filter(timestamp=split_timestamp(observation['effectiveDateTime']))[0] 
        elif observation['code']['text'] == 'Body mass index':
            if not BMI.objects.filter(timestamp=split_timestamp(observation['effectiveDateTime'])).exists():
                bmi = observation['valueQuantity']['value']
                ts = split_timestamp(observation['effectiveDateTime'])
                if bmi >= 30:
                    msg = 'Obese'
                elif bmi < 20:
                    msg = 'Underweight'
                elif bmi > 20 and bmi < 25:
                    msg = 'Tending towards underweight'
                elif bmi > 25 and bmi < 30:
                    msg = 'Overweight'
                elif bmi == 25:
                    msg = 'Normal'
                bmi_obj = BMI.objects.create(
                    patient_bmi = bmi,
                    timestamp = ts,
                    status = msg
                )
                bmi_obj.save()
            else:
                bmi_obj = BMI.objects.filter(timestamp=split_timestamp(observation['effectiveDateTime']))[0]

