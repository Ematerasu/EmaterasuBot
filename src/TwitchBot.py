import re
import asyncio
import random
import twitchio
import time
from twitchio.ext import commands, routines
from twitchio.ext.commands.errors import CommandOnCooldown
from urllib.parse import parse_qs, urlparse

from api.StreamElementsAPI import StreamElementsAPI
from api.TwitchAPI import TwitchAPI
from api.YoutubeAPI import YoutubeAPI

from config import (
    BANNED_VIDEOS,
    FURAZEK_EMOTES_LIST,
    SONG_REQUEST_SAVE_PLAYLISTS,
    STREAMELEMENTS_MAPPING,
    SUPPORTED_CHANNELS,
)
from responses import ADDED_SONG_RESPONSES, ERROR_SONG_RESPONSES

class EmaterasuBot(commands.Bot):

    valid_commands = ('Hejka', 'sr', 'ratujsr')

    def __init__(self, oauth_token: str):
        self.twitch_api = TwitchAPI()
        self.stream_elements_api = StreamElementsAPI()
        self.yt_api = YoutubeAPI()
        self.series_of_msgs = []
        self.flags = {
            'save_sr': (False, None)
        }
        super().__init__(token=oauth_token, prefix='%', initial_channels=SUPPORTED_CHANNELS)

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        chan = self.get_channel('FURAZEK')
        loop = asyncio.get_event_loop()
        loop.create_task(chan.send("Hejka wicowie ematerasu"))

    @routines.routine(hours=1)
    async def reset_token(self):
        print("Reset token start")
        self.twitch_api = TwitchAPI()
        print("Reset token finished")

    @commands.cooldown(rate=1, per=20, bucket=commands.Bucket.member)
    @commands.command()
    async def Hejka(self, ctx: commands.Context):
        await ctx.send(f'Hejka {ctx.author.name}!')

    @commands.cooldown(rate=5, per=600, bucket=commands.Bucket.member)
    @commands.command()
    async def sr(self, ctx: commands.Context):
        user_input = ctx.message.content.split(maxsplit=1)[1]
        query = self._parse_input(user_input) 
        if query['type'] == 'video':
            video_id = query['query']
            is_valid, error_response = self._check_link(user_input, ctx.author.name, ctx.message.tags['mod'] == '1')
            if not is_valid:
                await ctx.send(error_response)
                return
            channel_id = STREAMELEMENTS_MAPPING[ctx.channel.name]
            response = self.stream_elements_api.add_song(
                user_input,
                channel_id
            )
            print(f'{ctx.author.name} added song with id {video_id}. Response: {response.status_code}')
            if response.status_code >= 400:
                print(f'user_input: {user_input}')
                print(response.text)
                await ctx.send(f'@{ctx.author.name} ' + random.choice(ERROR_SONG_RESPONSES))
            elif 200 <= response.status_code < 300:
                await ctx.send(f'@{ctx.author.name} ' + random.choice(ADDED_SONG_RESPONSES))

        elif query['type'] == 'search':
            search_results = self.yt_api.search_videos(query['query'])
            channel_id = STREAMELEMENTS_MAPPING[ctx.channel.name]
            is_success = False
            for video_id, title in search_results:
                duration = self.yt_api.get_video_info(video_id)['items'][0]['contentDetails']['duration']
                if self._is_longer_than_10_minutes(duration):
                    continue
                response = self.stream_elements_api.add_song(
                    f'https://www.youtube.com/watch?v={video_id}',
                    channel_id
                )
                if response.status_code >= 400:
                    continue
                elif 200 <= response.status_code < 300:
                    print(f'{ctx.author.name} added song with id {video_id}. Response: {response.status_code}')
                    await ctx.send(f'@{ctx.author.name} ' + random.choice(ADDED_SONG_RESPONSES) + f' Link: https://www.youtube.com/watch?v={video_id} Tytuł: {title}')
                    is_success = True
                    break
            if not is_success:
                await ctx.send(f'@{ctx.author.name} ' + random.choice(ERROR_SONG_RESPONSES))

    @commands.cooldown(rate=1, per=1800, bucket=commands.Bucket.channel)
    @commands.command()
    async def ratujsr(self, ctx: commands.Context):
        if self.flags['save_sr'][0]: #if already enabled
            return
        
        if len(self.stream_elements_api.get_queue(STREAMELEMENTS_MAPPING[ctx.channel.name])) > 2:
            await ctx.send(f'@{ctx.author.name} tu nie ma co ratować, jest więcej niż 2 piosenki, może ktoś jeszcze dołoży aok')
            return

        self.flags['save_sr'] = (True, ctx.author.name)
        categories = ', '.join(SONG_REQUEST_SAVE_PLAYLISTS)
        await ctx.send(f'@{ctx.author.name} juz ratuje sr aok Powiedz mi tylko jaki tematyczny mix wrzucic. Aktualnie dostepne kategorie to: {categories}. By wybrać playliste wpisz tylko i wyłącznie jej nazwe.')

    async def event_message(self, message: twitchio.Message):
        if message.echo:
            return
        elif '@EmaterasuBot' == message.content:
            await message.channel.send(f'@{message.author.name} co aha')
        elif message.content.startswith('@EmaterasuBot kulki'):
            await message.channel.send('!play2')
            time.sleep(1)
            await message.channel.send('kulki Excitedgers')
        elif 'custom-reward-id' in message.tags and message.tags['custom-reward-id'] == 'd054e175-4dfa-4bc5-9e17-09409d9609bd':
            await self.handle_sr_prio_redeem(message)
        elif '!redeem zacoban' == message.content:
            await message.channel.send('za co ban aha')
        elif self.flags['save_sr'][0] and self.flags['save_sr'][1] == message.author.name:
            try:
                playlist = SONG_REQUEST_SAVE_PLAYLISTS[message.content]
            except KeyError:
                await message.channel.send(f'@{message.author.name} podaj prosze poprawna kategorie playlisty aha5 Tylko takie mam przygotowane Sadeg')
                self.flags['save_sr'] = (False, None)
                return
            channel_id = STREAMELEMENTS_MAPPING[message.channel.name]
            response = self.stream_elements_api.add_song(
                playlist,
                channel_id
            )
            print(f'{message.author.name} requested for playlist {playlist}. Response: {response.status_code}')
            if response.status_code >= 400:
                print(response.text)
                await message.channel.send('nie udało się uratować song requesta jasperSad spróbuj jeszcze raz użyć komendy')
            elif 200 <= response.status_code < 300:
                await message.channel.send('song request uratowany! jasperRADOSC')
            self.flags['save_sr'] = (False, None)
        elif not message.content.startswith('%'):
            msg = re.sub('[^A-Za-z0-9]+', ' ', message.content).strip() # parse and remove escape characters

            if not self.series_of_msgs or msg != self.series_of_msgs[-1]:
                if msg in FURAZEK_EMOTES_LIST:
                    self.series_of_msgs = [msg]
                else:
                    self.series_of_msgs = []
            elif msg == self.series_of_msgs[-1]:
                self.series_of_msgs.append(msg)

            if len(self.series_of_msgs) == 4:
                await message.channel.send(self.series_of_msgs[0])
                print(f'sent message: {self.series_of_msgs[0]}')
                self.series_of_msgs = []

        try:
            await self.handle_commands(message)
        except CommandOnCooldown:
            await message.channel.send('cooldown masz TSSK zaczekaj chwile')

    async def handle_commands(self, message):
        if message.content.startswith('%'):
            cmd = message.content.split()[0][1:]
            if cmd not in self.valid_commands:
                await message.channel.send(f'@{message.author.name} nie rozumiem aha Dostępne komendy: Hejka, sr <link do yt>, ratujsr')
                return
        return await super().handle_commands(message)

    async def handle_sr_prio_redeem(self, message):
        is_valid, error_response = self._check_link(message.content, message.author.name, message.tags['mod'] == '1')
        if not is_valid:
            await message.channel.send(error_response)

        channel_id = STREAMELEMENTS_MAPPING[message.channel.name]
        try:
            response = self.stream_elements_api.add_song_at(
                message.content,
                0,
                channel_id
            )
            print(f'{message.author.name} added song with prio. Response: {response.status_code}')
            if response.status_code >= 400:
                await message.channel.send(f'@{message.author.name} nie udało się dodać na szczyt listy SadCat Niech jakiś mod zwróci punkty')
            elif 200 <= response.status_code < 300:
                await message.channel.send(f'@{message.author.name} ' + random.choice(ADDED_SONG_RESPONSES))
        except:
            await message.channel.send(f'@{message.author.name} nie udało się dodać na szczyt listy SadCat Niech jakiś mod zwróci punkty')
        

    async def close(self):
        chan = self.get_channel('FURAZEK')
        loop = asyncio.get_event_loop()
        loop.create_task(chan.send("ide spać dobranoc papa NewOutfit"))
        await super().close()

    def _check_link(self, video_url, author_name, is_mod):
        if not self._is_link_valid(video_url):
            return False, f'@{author_name} link jest nieprawidlowy jasperSad'
        video_id = self._get_video_id(video_url)
        if video_id in BANNED_VIDEOS:
            return False, f'@{author_name} zultakartka film jest zbanowany'
        video_info = self.yt_api.get_video_info(video_id)
        if not video_info['items']:
            return False, f'@{author_name} link nie działa jasperSad'
        if is_mod:
            return True, ''
        duration = video_info['items'][0]['contentDetails']['duration']
        if self._is_longer_than_10_minutes(duration):
            return False, f'@{author_name} filmik jest za długi posluchajdzieciaku max 10 minut'
        if int(video_info['items'][0]['statistics']['viewCount']) < 5000:
            return False, f'@{author_name} filmik ma za mało wyświetleń. Wymagane jest conajmniej 5k tssk'
        return True, ''

    def _is_link_valid(self, link):
        if '&list=' in link:
            return False
        pattern = r'(https?://)?(www\.)?((youtube\.com/watch\?v=)|(youtu.be/))[a-zA-Z0-9_-]{11}'
        return re.match(pattern, link)
    
    def _is_longer_than_10_minutes(self, duration):
        duration_regex = r'^PT((\d+)H)?((\d+)M)?(\d+)S$'
        match = re.match(duration_regex, duration)
        if not match:
            # If the duration doesn't match the expected format, assume it's not longer than 10 minutes
            return False
        else:
            hours = int(match.group(2) or 0)
            minutes = int(match.group(4) or 0)
            seconds = int(match.group(5))
            if hours * 60 + minutes + seconds / 60 > 10:
                return True
            else:
                return False

    def _parse_input(self, input_str):
        if 'youtube.com/' in input_str or 'youtu.be/' in input_str:
            video_id = self._get_video_id(input_str)
            return {'type': 'video', 'query': video_id}
        else:
            return {'type': 'search', 'query': input_str}

    def _get_video_id(self, video_url):
        if 'youtu.be/' in video_url:
            return video_url.split('/')[-1]
        try:
            return parse_qs(urlparse(video_url).query)['v'][0]
        except KeyError:
            return video_url.split('/')[-1].split('?')[0]
