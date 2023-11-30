import requests

class SevenTVAPI:

    BASE_URL = 'https://emotes.adamcy.pl/v1/channel/FURAZEK/emotes/all'

    def __init__(self):
        self.emotes = []
        self._get_furazek_emote_set()

    def refresh(self):
        self._get_furazek_emote_set()

    def _get_furazek_emote_set(self):
        res = requests.get(self.BASE_URL)
        if res.status_code != 200:
            return
        emotes = []
        for emote in res.json():
            emotes.append(emote['code'])
        self.emotes = tuple(emotes)
    
