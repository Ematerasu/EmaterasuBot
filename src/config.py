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