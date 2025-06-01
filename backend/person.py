import requests
from util import *
import json
from collections import Counter
from secret import API_KEY, SHARED_SECRET, USER_AGENT

class Person():
    def __init__(self):
        # user data
        self.name = "no_name"
        self.pfp = "no_pfp"

        # artist + genre data
        self.artist_names = []
        self.genres = []

        # track data
        self.track_names = []
        self.track_artists = []

        # album data
        self.album = "no_album"
        self.album_pfp = "no_album_pfp"
        self.album_artist = "no_album_artist"

        # popularity data
        self.popularity = 0

        # recommendations
        self.rec_artist = "no_rec_artist"
        self.rec_track = "no_rec_track"
    
    def to_json(self):
        my_dict = self.__dict__
        del my_dict['header']
        return my_dict
    
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
    def __init__(self, headers, playlist):
        super().__init__()
        self.playlist = playlist[34:56]
        self.header = headers
        self.initialize_partner()
    
    def initialize_partner(self):
        playlist_response = requests.get(f"{BASE_URL}/playlists/{self.playlist}", headers=self.header)
        playlist_data = playlist_response.response_text if playlist_response.status_code != 200 else playlist_response.json()
        
        # user data
        self.name=playlist_data["owner"]["display_name"]
        user_id = playlist_data["owner"]["id"]
        user_response = requests.get(f"{BASE_URL}/users/{user_id}", headers=self.header)
        user_data = user_response.response_text if user_response.status_code != 200 else user_response.json()
        if user_data["images"]:
            self.pfp = user_data["images"][0]["url"]

        artist_ids = []
        track_pop = 0
        for t in playlist_data['tracks']['items']:
            # track data
            if len(self.track_names) < 5:
                self.track_names.append(t['track']['name'])
                self.track_artists.append(t['track']['artists'][0]['name'])

                # album data
                if self.album == "no_album":
                    self.album = t['track']['album']['name']
                    self.album_artist = t['track']['album']['artists'][0]['name']
                    self.album_pfp = t['track']['album']['images'][0]['url']

            # artist data
            track_pop += t['track']['popularity']
            artist_ids.append(t['track']['artists'][0]['id'])
            self.artist_names.append(t['track']['artists'][0]['name'])
        
        self.artist_names = [a for a, cnt in Counter(self.artist_names).most_common(3)]
        
        # genre data
        artist_ids = list(set(artist_ids))[:49]
        aid_str = ",".join(artist_ids)
        artist_response = requests.get(f"{BASE_URL}/artists", params={"ids": aid_str}, headers=self.header)
        artist_data = artist_response.response_text if artist_response.status_code != 200 else artist_response.json()
        
        artist_pop = 0
        for a in artist_data['artists']:
            artist_pop += a['popularity']
            if a['genres']:
                self.genres.append(a['genres'][0])
        self.genres = [g for g, cnt in Counter(self.genres).most_common(5)]
        
        # popularity data
        self.popularity = (track_pop + artist_pop) // (len(playlist_data['tracks']['items']) + len(artist_data['artists']))

        # recommendations
        self.rec_artist = self.similar_artist(self.artist_names[0])
        self.rec_track = self.similar_track(track=self.track_names[0], artist=self.track_artists[0])