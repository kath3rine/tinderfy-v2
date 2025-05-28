import requests
from secret import API_KEY, SHARED_SECRET, USER_AGENT

class Match():
    def __init__(self, shared_artist):
        self.rec_artist = self.get_similar_artist(shared_artist)
    
    def get_similar_artist(self, artist):
        headers = {'user_agent': USER_AGENT}
        url = 'https://ws.audioscrobbler.com/2.0/'
        payload = {
            'api_key': API_KEY,
            'format': 'json',
            'method': 'artist.getsimilar',
            'artist': artist
        }

        data = requests.get(url, headers=headers, params=payload)
        data = data.json()
        return data['similarartists']['artist'][0]['name']


