
# Onpatient Vital Signs Tracker

A good starting point: https://github.com/drchrono/api-example-django

IMPORTANT: 
- This project was built using Python 2.7.14 and Django 1.11.6. Compatibility with Python 3.x is NOT guaranteed.
- The starter code is built using Python 2.7.x and Django 1.8.3. It also uses an older version of python-social-auth (0.2.21) which has some significant differences when compared to the latest version (0.3.6). Make sure to follow the instructions [here](https://github.com/omab/python-social-auth/blob/master/MIGRATING_TO_SOCIAL.md#django) in order to ensure successful migration to the newer version.

### Requirements

- [pip](https://pip.pypa.io/en/stable/)
- [python virtual env](https://packaging.python.org/installing/#creating-and-using-virtual-environments)
- All packages to be installed inside the virtual environment are in requirements.txt.

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

### Changelog

11/16/17:
- The post-login landing page is the latest to receive a major facelift! This is a partial update, with the rest of it (along with updates for the trackers) coming shortly. Kudos once again to the [Bootstrap](http://getbootstrap.com/) team.

11/15/17:
- Compatibility with Django 1.11.7 tested. Works without issues.
- Cool new front-end for the login page! Thanks to the [Bootstrap](http://getbootstrap.com/) team. Front-end for the rest of the application coming soon.
