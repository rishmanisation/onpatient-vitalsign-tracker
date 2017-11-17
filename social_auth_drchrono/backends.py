import os
from social.backends.oauth import BaseOAuth2

class onpatientOAuth2(BaseOAuth2):
    """
    onpatient OAuth authentication backend
    """

    name = 'onpatient'
    ID_KEY = 'username'
    AUTHORIZATION_URL = 'https://onpatient.com/o/authorize/'
    ACCESS_TOKEN_URL = 'https://onpatient.com/o/token/'
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False
    USER_DATA_URL = 'https://drchrono.com/onpatient_api/fhir/Patient'
    EXTRA_DATA = [
        ('refresh_token', 'refresh_token'),
        ('expires_in', 'expires_in')
    ]
    # TODO: setup proper token refreshing

    def get_user_details(self, response):
        """
        Return user details from onpatient account
        """
        return {'username': response.get('username'),}

    def user_data(self, access_token, *args, **kwargs):
        """
        Load user data from the service
        """
        return self.get_json(
            self.USER_DATA_URL,
            headers=self.get_auth_header(access_token)
        )

    def get_auth_header(self, access_token):
        return {'Authorization': 'Bearer {0}'.format(access_token)}
