from flask import Flask, session, redirect, request, jsonify
from flask_cors import CORS
from util import *
import json
import requests
from person import User, Match
from secret import CLIENT_ID, CLIENT_SECRET

REDIRECT_URI = "http://localhost:5000/callback"
SCOPE = "user-top-read user-library-read user-read-private user-read-email"

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:3000"])
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

    if response.status_code != 200:
        return response.text
    
    response = response.json()
    session['tokens'] = {
        'access_token': response.get('access_token'),
        'refresh_token': response.get('refresh_token'),
    }

    return redirect('/user')

# user's tinder profile
@app.route('/user', methods=['GET'])
def me():
    if 'tokens' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    headers = {'Authorization': f"Bearer {session['tokens'].get('access_token')}"}
    
    user = User(headers)
    session['user'] = user.__dict__

    return session['user']

# enter other user's info
@app.route('/match', methods=['POST'])
def match():
    data = request.json
    pid = data.get('pid')

    if not pid:
        return jsonify({"message": "error no pid"})
    elif not session['user']:
        return jsonify({"message": "no session user"})
    
    match = Match(pid, session['user'])
    response = match.__dict__
    
    return jsonify({"message": response})


    
if __name__ == '__main__':
    app.run(debug=True, host="localhost")