from flask import Flask, session, redirect, request
from util import *
import requests
from user import User
from match import Match
from secret import CLIENT_ID, CLIENT_SECRET

REDIRECT_URI = "http://127.0.0.1:5000/callback"
SCOPE = "user-top-read user-library-read user-read-private user-read-email"

app = Flask(__name__)
app.secret_key = "secretkey"

# log into spotify
@app.route('/')
def login():
    auth_url = (
        f"{AUTH_URL}?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope={SCOPE}"
    )
    return redirect(auth_url)

# spotify auth
@app.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return "authorization failed"
    
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    response = requests.post(TOKEN_URL, data=payload)
    response = response.json()
    session['tokens'] = {
        'access_token': response.get('access_token'),
        'refresh_token': response.get('refresh_token'),
    }

    return redirect('/me')

# user's tinder profile
@app.route('/me')
def me():
    headers = {'Authorization': f"Bearer {session['tokens'].get('access_token')}"}
    
    user = User(headers)
    
    
    tracks = user.tracks
    artists = user.artists
    match = Match(artists["names"][4])
    rec = match.rec_artist

    artist_str = f"top artists: {artists['names']}"
    genre_str = f"top genres: {artists['genres']}"
    track_str = f"top tracks: {tracks['titles']} by {tracks['artists']}"
    rec_str = f"recommended arrist: {rec}"

    return f"{artist_str}{genre_str}{track_str}{rec_str}"

# enter other user's info
@app.route('/match')
def match():
    return redirect('/result')

# results of compatibility assessment
@app.route('/result')
def result():
    return result

    
if __name__ == '__main__':
    app.run(debug=True)