import os
from dotenv import load_dotenv
from api.StreamElementsAPI import StreamElementsAPI
from api.TwitchAPI import TwitchAPI
from api.YoutubeAPI import YoutubeAPI

from TwitchBot import EmaterasuBot

if __name__ == '__main__':
    load_dotenv()
    oauth_token = os.getenv('TWITCH_OAUTH_TOKEN')
    bot = EmaterasuBot(oauth_token)
    _task = bot.reset_token.start()

    try:
        bot.run()
    except KeyboardInterrupt:
        print('closing')
        bot.close()
