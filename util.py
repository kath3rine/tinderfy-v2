import urllib
import requests
from secret import CLIENT_ID, CLIENT_SECRET

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token/'
BASE_URL = 'https://api.spotify.com/v1/'

REDIRECT_URI = "http://127.0.0.1:5000/"

def get_auth_url():
    print("getting auth url")
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        'scope': 'user-library-read user-top-read'
    }
    return f'{AUTH_URL}/?{urllib.parse.urlencode(params)}'

def get_access_token(auth_code):
    print("getting access token")
    body = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': REDIRECT_URI
    }
    response = requests.post(TOKEN_URL, auth=(CLIENT_ID, CLIENT_SECRET), data=body)
    if response.status_code==200:
        return response.json()
    raise Exception("failed to get access token")