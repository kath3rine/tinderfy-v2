## About
Spotify Wrapped meets dating app. Display your Spotify stats in a Tinder profile and compare your music taste with another person's.

Features
<li> Most listened to artists, songs, genres, album
<li> Artists and genres that two people both listen to
<li> How unique/uncommon someone's favorite music is
<li> Recommended song and/or artist based on person's favorite music

## Demos
<a href="https://drive.google.com/file/d/14A3Os4FH-SMW-iZzdGd18q14dg02a5Lr/view?usp=sharing">demo video link</a>

User's stats
![user screen](./images/user-screen.png)

Partner's stats:
![match screen](images/match-screen.png)
![submission form](images/submit-screen.png)

Side-by-side: real Tinder UI
![side by side 1](images/comparison1.png)
![side by side 2](images/comparison2.png)

## How to use
<li> Ensure you have Flask, React, and Python installed
<li> Execute 'flask run' in the backend sub-directory, and 'npm start' in the frontend sub-directory
<li> Go to http://localhost:3000/ in your browser
<li> Log into your Spotify account when prompted. You should see your Spotify stats.
<li> To compare yourself with someone else, click Match on the bottom sidebar, and enter the URL of another their playlist

## Tech
Frontend: React (HTML, CSS, Javascript) <br>
Backend: Flask (Python), API (Spotify, Last.fm) <br>
Old version (not compatible with new Spotify API): https://github.com/kath3rine/tinderfy

