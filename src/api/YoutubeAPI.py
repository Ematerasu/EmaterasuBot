import os
import requests

from utils.utils import pretty_print_dict

class YoutubeAPI:

    base_url = 'https://www.googleapis.com/youtube/v3/'

    def __init__(self):
        self.api_key = os.getenv('YOUTUBE_API_KEY')

    def get_video_info(self, video_id):
        endpoint = f'{self.base_url}videos?part=contentDetails,statistics&id={video_id}&key={self.api_key}'
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text
    
    def search_videos(self, prompt):
        endpoint = f'{self.base_url}search?part=snippet&q={prompt}&key={self.api_key}'
        response = requests.get(endpoint)
        if response.status_code == 200:
            data = response.json()
            videos = []
            pretty_print_dict(data)
            for item in data['items']:
                if item['id']['kind'] == 'youtube#video':
                    video_id = item['id']['videoId']
                    title = item['snippet']['title']
                    videos.append((video_id, title))
            return videos
        else:
            return None