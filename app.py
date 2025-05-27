from flask import Flask, session, make_response, redirect, request
from urllib.parse import urlencode
from util import *
import requests
from user import User
from playlist import Playlist
from secret import CLIENT_ID, CLIENT_SECRET

REDIRECT_URI = "http://127.0.0.1:5000/callback"

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
    tmp = "5KBKqxYY263Tr0haAu3fMz"
    headers = {'Authorization': f"Bearer {session['tokens'].get('access_token')}"}
    
    #playlist = Playlist(headers, "11dFghVXANMlKmJXsNCbNl")
    #return str(playlist.test)
    #return str(playlist.test)
    user = User(headers)
    #return f"track: {user.tid} data: {str(user.test)}"
    artists = user.artist_names
    genres = user.genres
    name = user.name
    albums = user.albums
    tracks = user.track_titles
    track_artists = user.track_artists
    return f"Name: {str(name)}, Top Artists: {str(artists)[1:-1]}, Top Albums: {str(albums)}, Top Genres: {str(genres)}, Tracks: {str(tracks)}, Track Artists: {str(track_artists)}"
    
if __name__ == '__main__':
    app.run(debug=True)