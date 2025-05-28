import requests
import json
from util import *
from secret import API_KEY, SHARED_SECRET, USER_AGENT

class Person():
    def __init__(self):
        # user data
        self.name = "default_name"
        self.pfp = None

        # artist + genre data
        self.artist_names = []
        self.genres = []

        # track data
        self.track_names = []
        self.track_artists = []

        # album data
        self.album = "no_album"
        self.album_pfp = None
        self.album_artist = None

        # popularity data
        self.popularity = 0

        # recommendations
        self.rec_artist = "no_artist"
        self.rec_track = "no_track"
    
    def to_json(self):
        my_dict = self.__dict__
        del my_dict['header']
        return json.dumps(my_dict, indent=2)
    
    # methods for using lastfm api 
    def lastfm_api(self, method: str, parameters: list):
        headers = {'user_agent': USER_AGENT}
        url = 'https://ws.audioscrobbler.com/2.0/'
        payload = {
            'api_key': API_KEY,
            'format': 'json',
            'method': method,
        }

        for k, v in parameters:
            payload[k] = v

        data = requests.get(url, headers=headers, params=payload)
        return data.json()
    
    def similar_artist(self, artist):
        data = self.lastfm_api(method='artist.getsimilar', parameters=[('artist', artist)])
        return data['similarartists']['artist'][0]['name']
    
    def similar_track(self, artist, track):
        data = self.lastfm_api(method='track.getsimilar', parameters=[('artist', artist), ('track', track)])
        if data['similartracks']['track']:
            rec = data['similartracks']['track'][0]
            return f"{rec['name']} by {rec['artist']['name']}"
        return f"None"

class User(Person):
    def __init__(self, headers):
        super().__init__()
        self.header = headers
        self.initialize_user()
    
    # fetch data from the /me/ endpoint
    def get_my_data(self, param):
        data = requests.get(f"{BASE_URL}/me/{param}", headers=self.header)
        if data.status_code != 200:
            return data.response_text
        return data.json()
    
    def initialize_user(self):
        # user data
        user_data = self.get_my_data("")
        self.name = user_data['display_name'],
        self.pfp = user_data['images'][0]['url']

        # artist + genre data
        artist_pop = 0
        artist_data = self.get_my_data("top/artists?limit=10")
        for a in artist_data['items']:
            self.artist_names.append(a['name'])
            artist_pop += a['popularity']
            if a['genres']:
                self.genres.append(a['genres'][0])
            self.genres = list(dict.fromkeys(self.genres))[:5]

        # track data
        track_pop = 0
        track_data = self.get_my_data("top/tracks?limit=5")
        for t in track_data['items']:
            self.track_names.append(t['name'])
            self.track_artists.append(t['artists'][0]['name'])
            track_pop += t['popularity']
        
        # popularity data
        self.popularity = (track_pop + artist_pop) // (len(self.track_names) + len(self.artist_names))
        
        # album data
        album_data = self.get_my_data("albums?limit=1")['items'][0]['album']
        self.album = album_data['name']
        self.album_pfp = album_data['images'][0]['url']
        self.album_artist = album_data['artists'][0]['name']

        # recommendations
        self.rec_artist = self.similar_artist(self.artist_names[0])
        self.rec_track = self.similar_track(track=self.track_names[0], artist=self.track_artists[0])
    
class Partner(Person):
    def __init__(self, headers, pid, name):
        super().__init__()
        self.header = headers
    
    def initialize_partner(self):
        return




    
    