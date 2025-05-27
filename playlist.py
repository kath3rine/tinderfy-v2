import pandas as pd
import requests
from util import *

class Playlist:
    def __init__(self, header, tid):
        self.header = header
        self.test = self.get_track_audio(tid)
    
    def get_track_audio(self, tid):
        data = requests.get(f"{BASE_URL}audio-features/{tid}", headers=self.header)
        data = data.json()

        #feature_lst = ["danceability", "acousticness"]
        #features = [data[ft] for ft in feature_lst]
        return data
