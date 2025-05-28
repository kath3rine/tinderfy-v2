import requests
import json
from util import *
from secret import API_KEY, SHARED_SECRET, USER_AGENT
from abc import ABC, abstractmethod

class Person():
    def __init__(self):
        # user data
        self.name = "default_name"
        self.pfp = None

        # artist + genre data
        self.artist_names = []
        self.artist_ids = []
        self.genres = []

        # track data
        self.track_names = []
        self.track_ids = []
        self.track_artists = []

        # album data
        self.album = None

        # popularity data
        self.popularity = 0
    
    @abstractmethod
    def initialize():
        pass
    
    def to_json(self):
        my_dict = self.__dict__
        del my_dict['header']
        return json.dumps(my_dict, indent=2)

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
        artist_data = self.get_my_data("top/artists?limit=5")
        for a in artist_data['items']:
            self.artist_names.append(a['name'])
            self.artist_ids.append(a['id'])
            artist_pop += a['popularity']
            if a['genres']:
                self.genres.append(a['genres'][0])

        # track data
        track_pop = 0
        track_data = self.get_my_data("top/tracks?limit=5")
        for t in track_data['items']:
            self.track_names.append(t['name'])
            self.track_artists.append(t['artists'][0]['name'])
            self.track_ids.append(t['id'])
            track_pop += t['popularity']
        
        # popularity data
        self.popularity = (track_pop + artist_pop) // 10
        
        # album data
        album_data = self.get_my_data("albums?limit=1")
        self.album = album_data['items'][0]['album']['name']
    





    
    