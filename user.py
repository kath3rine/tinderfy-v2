from util import *

class User():
    USER_URL = f"{BASE_URL}me/"

    def __init__(self, header):
        self.header = header
        self.name = self.get_user()[0]
        self.pfp = self.get_user()[1]
        self.artist_names = self.get_artists()[0]
        self.artist_ids = self.get_artists()[1]
        self.genres = self.get_artists()[2]
        self.track_names = self.get_tracks()[0]
        self.track_ids = self.get_tracks()[1]
        self.albums = self.get_albums()
    
    def get_user(self): # returns tuple {username, pfp}
        data = requests.get(f"{BASE_URL}me", headers=self.header)
        data = data.json()
        return (data['display_name'], get_image(data))
    
    def get_artists(self): # returns tuple of lists (top artist names, top artist ids, top genres)
        data = requests.get(f"{BASE_URL}me/top/artists?limit=5", headers=self.header)
        data = data.json()
        names = [a['name'] for a in data['items']]
        ids = [a['id'] for a in data['items']]
        genres = [a['genres'][0] for a in data['items']]
        genres = list(dict.fromkeys(genres))
        return (names, ids, genres)
    
    def get_tracks(self): # returns tuple of lists (top track names, top track ids)
        data = requests.get(f"{BASE_URL}me/top/tracks", headers=self.header)
        data = data.json()
        names = [t['name'] for t in data['items']]
        ids = [t['id'] for t in data['items']]
        return (names, ids)
    
    def get_albums(self):
        data = requests.get(f"{BASE_URL}me/albums?limit=5", headers=self.header)
        data = data.json()
        albums = [a['album']['name'] for a in data['items']]
        return albums

    
    