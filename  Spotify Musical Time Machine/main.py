from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth
import spotipy

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='    ',
    client_secret='  ',
    redirect_uri='https://example.com/callback',    #'http://localhost:8888/callback',
    scope='playlist-modify-public'
))

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


# user_id = sp.current_user()["id"]
user_id = sp.me()['id']


playlist_name = 'f{date} Billboard 100'
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
playlist_id = playlist['id']


track_uris = []
for song in song_names:
    result = sp.search(q=song, type='track', limit=1)
    tracks = result.get('tracks', {}).get('items', [])
    if tracks:
        track_uris.append(tracks[0]['uri'])
        print(f"Added: {tracks[0]['name']}")
    else:
        print(f"Not found: {song}")

# Step 6: Add tracks to the playlist
if track_uris:
    sp.playlist_add_items(playlist_id, track_uris)
    print(f"\nPlaylist '{playlist_name}' created and populated!")
else:
    print("No tracks found to add.")

