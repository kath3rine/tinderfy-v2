import requests
from util import *

class User():
    def __init__(self, header):
        self.header = header

        self.name = self.get_user()["name"]
        self.pfp = self.get_user()["pfp"]

        self.artist_names = self.get_artists()["names"]
        self.artist_ids = self.get_artists()["ids"]
        self.genres = self.get_artists()["genres"]

        self.track_titles = self.get_tracks()["titles"]
        self.track_ids = self.get_tracks()["ids"]
        self.track_artists = self.get_tracks()["artists"]

        self.albums = self.get_albums()
    
    def get_my_data(self, param):
        data = requests.get(f"{BASE_URL}me/{param}", headers=self.header)
        return data.json()
    
    def get_user(self): 
        data = self.get_my_data("")
        return {"name": data['display_name'],
             "pfp": data['images'][0]['url']}
    
    def get_artists(self): 
        data = self.get_my_data("top/artists?limit=5")
        names = [a['name'] for a in data['items']]
        ids = [a['id'] for a in data['items']]

        genres = set()
        for a in data['items']:
            if a['genres']:
                genres.add(a['genres'][0])
    
        return {"names": names,
             "ids": ids,
             "genres": genres}
    
    def get_tracks(self): 
        data = self.get_my_data("top/tracks?limit=5")
        return {"titles": [t['name'] for t in data['items']],
               "artists": [t['artists'][0]['name'] for t in data['items']],
               "ids": [t['id'] for t in data['items']]}
    
    def get_albums(self):
        data = self.get_my_data("albums?limit=5")
        return [a['album']['name'] for a in data['items']]





    
    