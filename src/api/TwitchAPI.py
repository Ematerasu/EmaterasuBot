import os
import requests


class TwitchAPI:

    AUTH_URL = 'https://id.twitch.tv/oauth2/token'
    API_URL = 'https://api.twitch.tv/helix/'

    def __init__(self):
        self.access_token = os.getenv('TWITCH_ACCESS_TOKEN')
        self.client_id = os.getenv('CLIENT_ID')
        self.api_token = self._authenticate()

    def _authenticate(self):
        auth_params = {
            'client_id': self.client_id,
            'client_secret': self.access_token,
            'grant_type': 'client_credentials'
        }

        response = requests.post(url=self.AUTH_URL, params=auth_params)
        return response.json()['access_token']


    def get_headers(self):
        return {
            'Authorization': f'Bearer {self.api_token}',
            'Client-ID': self.client_id,
        }
    
    def get(self, query):
        print(f"GET request on {self.API_URL+query}")
        response = requests.get(self.API_URL+query, headers=self.get_headers())
        return response
    
    def user_info(self, login):
        response = requests.get(f'https://api.twitch.tv/helix/users?login={login}', headers=self.get_headers())
        return response.json()
    
    def validate_token(self):
        response = requests.get('https://id.twitch.tv/oauth2/validate', headers=self.get_headers())
        if response.status_code == 200:
            return True
        else:
            print(f'Token is invalid: {response.text}')
            return False

    def get_channel_info(self, channel_id):
        url = 'https://api.twitch.tv/helix/channels'
        params = {'broadcaster_id': channel_id}
        response = requests.get(url, params=params, headers=self.get_headers())
        print(response.text)