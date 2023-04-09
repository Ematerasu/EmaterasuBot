import os

import requests


class StreamElementsAPI:
    BASE_URL = 'https://api.streamelements.com/kappa/v2/'

    def __init__(self):
        self.jwt_token = os.getenv('EMATERASU_STREAM_ELEMENTS_JWT_TOKEN')
        self.account_id = os.getenv('EMATERASU_STREAM_ELEMENT_ACCOUNT_ID')

    def get_queue(self, channel_id: str =''):
        endpoint = f'songrequest/{channel_id if channel_id else self.account_id}/queue'
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.jwt_token}'
        }
        response = requests.get(self.BASE_URL+endpoint, headers=headers)
        return response.json()
    
    def add_song(self, video_id: str, channel_id: str =''):
        endpoint = f'songrequest/{channel_id if channel_id else self.account_id}/queue'
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.jwt_token}'
        }

        body = {
            'video': video_id,
            'top': True,
        }
        response = requests.post(self.BASE_URL+endpoint, json=body, headers=headers)
        return response
    
    def add_song_at(self, video_id: str, position: int, channel_id: str):
        response_post = self.add_song(video_id, channel_id)
        song_id = response_post.json().get('_id')
        if not song_id:
            raise Exception('did not receive id')
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.jwt_token}'
        }
        endpoint = f'songrequest/{channel_id}/queue/{song_id}'
        response = requests.put(self.BASE_URL+endpoint, json={'position': position}, headers=headers)
        return response