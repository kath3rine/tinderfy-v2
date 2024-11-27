from flask import Flask, session, make_response, redirect, request
# from util import *
from urllib.parse import urlencode
import requests
from secret import CLIENT_ID, CLIENT_SECRET

REDIRECT_URI = "http://127.0.0.1:5000/callback"

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def login():
    payload = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI, 
        'scope': 'user-top-read user-library-read'
    }
    return make_response(redirect(f'{AUTH_URL}/?{urlencode(payload)}'))

@app.route('/callback')
def callback():
    code = request.args.get('code')
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
    }

    response = requests.post(TOKEN_URL, auth=(CLIENT_ID, CLIENT_SECRET), data=payload)
    response = response.json()
    session['tokens'] = {
        'access_token': response.get('access_token'),
        'refresh_token': response.get('refresh_token'),
    }

    return redirect('/profile')

@app.route('/profile')
def profile():
    headers = {'Authorization': f"Bearer {session['tokens'].get('access_token')}"}

    top_artists_params = { 'limit': 10 }
    top_artists = requests.get(f"{BASE_URL}me/top/artists?limit=10", headers=headers)
    top_artists = top_artists.json()
    top_artists_names = []
    for a in top_artists['items']:
        top_artists_names.append(a['name'])
    return top_artists_names
