import requests

class XayoAPI:

    BASE_URL = 'https://xayo.pl/api/mostWatched/'

    @classmethod
    def get_watchtime(cls, user: str):
        resp = requests.get(cls.BASE_URL + user)
        if resp.status_code != 200:
            return None
        channels = [item['streamer'] for item in resp.json()[:5]]
        return channels
