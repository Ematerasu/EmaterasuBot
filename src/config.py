import os
from dotenv import load_dotenv

load_dotenv()

SUPPORTED_CHANNELS = (
    'ematerasu__',
    'furazek'
)

STREAMELEMENTS_MAPPING = {
    'ematerasu__': os.getenv('EMATERASU_STREAM_ELEMENT_ACCOUNT_ID'),
    'furazek': os.getenv('FURAZEK_STREAM_ELEMENT_ACCOUNT_ID')
}

TWITCH_ID_MAPPING = {
    'ematerasu__': '47911419',
    'furazek': '89709140',
    'EmaterasuBot': '896496342'
}

BANNED_VIDEOS = (
    'nUCT0YeNCgE', 'rcVb6l4TpHw', 'k7WnXmOFR8I', 'h6V74FuW4Ac', '8ddRoYK4X80', 'NjD0H4eBfng',
    '2EqINpSNOPM', 'uxZoH0H74HI', '6BzWjuDK_kA', 'pceHY7rkiTg', 'Y2qsl0z-NBk', 'CWmI_4SkrD0',
    'myIvgyeVXMo', 'YG4iTGjuoKw', 'scXlu4staJA', 'YyUGPRRB42A'
)

SONG_REQUEST_SAVE_PLAYLISTS = {
    'eska': 'https://www.youtube.com/watch?v=7C-Ky2D2lZE',
    'nightclub': 'https://www.youtube.com/watch?v=MehaUz9s5MY',
    'techno': 'https://www.youtube.com/watch?v=w1lc8LKgLIY',
    'rap': 'https://www.youtube.com/watch?v=a0pexLfjn-s',
    'disco': 'https://www.youtube.com/watch?v=VodMgPR74UQ',
    'phonk': 'https://www.youtube.com/watch?v=phuY3ucYk88',
}

WYMOWKI = (
    'Rodzina przyjechala',
    'Wychodze z Paulina',
    'Dzieci przyszly do domu',
    'Czas z Paulina',
    'Gralem do nocy',
    'Plecy bola',
    'Nie ma co robic',
    'Nic sie nie dzieje',
    'Niedobrze mi',
    'Nie wyspałem się',
    'W kolejce jestem',
    'Glowa boli od lekow',
    'Brzuch boli od leków',
    'Lekarza mam'
)

CUSTOM_REWARD_MAPPING = {
    'furazek': {
        'song_request_prio': 'd054e175-4dfa-4bc5-9e17-09409d9609bd',
        'vol100': None,
        'timeout': '55b4599c-b7b9-4a3b-bdb6-571c3b7fcc04',
    },
    'ematerasu__': {
        'song_request_prio': '36634d5b-b01a-46de-b22a-1b41b515ea9b',
        'vol100': '33e98c13-c227-4c52-adf0-d1bde424912f',
        'timeout': 'c097aa27-d5c4-47a5-b504-350a45020638',
    }
}