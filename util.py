import requests

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

def get_data(item_id, item_type, header):
    data = requests.get(BASE_URL + item_type + '/' + item_id, headers=header)
    return data.json() 

def get_image(data):
    return data['images'][0]['url']