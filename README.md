# Onpatient Vital Signs Tracker

Cloned from: https://github.com/drchrono/api-example-django

IMPORTANT: This project was built using Python 2.7.14 and Django 1.11.6. Compatibility with Python 3.x and Django 1.8.3 is NOT guaranteed.

### Requirements

- [pip](https://pip.pypa.io/en/stable/)
- [python virtual env](https://packaging.python.org/installing/#creating-and-using-virtual-environments)

### Setup

Use of a virtual environment is highly recommended. For instructions on how to install and setup a virtual environment, see the link above.

Within your virtual environment, run the following commands:

``` bash
$ pip install -r requirements.txt
$ python manage.py makemigrations health_app 
$ python manage.py sqlmigrate health_app x 
$ python manage.py migrate
$ python manage.py runserver
```

NOTE: These commands were tested on Windows 10. They should run just fine on bash as well.

Lines 2 and 3 only need to be executed on the first run or if any changes are made to models.py. In line 2, replace 'x' with the migration number (ex: 0001). See the migrations folder within health_app for the most recent migration.

`social_auth_drchrono/` contains a custom provider for [Python Social Auth](http://python-social-auth.readthedocs.io/en/latest/) that handles OAUTH for onpatient. To configure it, set these fields in your `drchrono/settings.py` file:

```
SOCIAL_AUTH_ONPATIENT_KEY
SOCIAL_AUTH_ONPATIENT_SECRET
SOCIAL_AUTH_ONPATIENT_SCOPE
LOGIN_REDIRECT_URL
```
