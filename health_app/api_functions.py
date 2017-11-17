import requests

def get_patient(social):

    patients = []
    patients_url = 'https://drchrono.com/onpatient_api/fhir/Patient'
    headers = {
        'Authorization': 'Bearer %s' % social.extra_data['access_token']
        }

    while patients_url:
        data = requests.get(patients_url, headers=headers)

        # Check for the case of no patients
        if not data:
            break

        json_data = data.json()
        patients.extend(json_data['results'])
        patients_url = json_data['next']  # A JSON null on the last page

    return patients

def get_observations(social):

    observations = []
    obs_url = 'https://drchrono.com/onpatient_api/fhir/Observation'
    headers = {
        'Authorization': 'Bearer %s' % social.extra_data['access_token']
    }

    while obs_url:
        data = requests.get(obs_url, headers=headers)
        if not data:
            break
    
        json_data = data.json()
        observations.extend(json_data['results'])
        obs_url = json_data['next']
    
    return observations




