import requests
import base64
import sys
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
 

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = 'http://localhost:5000/callback'
scope = "playlist-read-private user-read-private playlist-modify-public playlist-modify-private user-library-read user-top-read"

sp = spotipy.Spotify(auth_manager= SpotifyOAuth(client_id = client_id,client_secret = client_secret,redirect_uri = redirect_uri,scope = scope))

# function to search tracks of your choice
def search_track(token, track_name):
    search_url = f'https://api.spotify.com/v1/search?q={track_name}&type=track&limit=10'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    search_response = requests.get(search_url, headers=headers)

    if search_response.status_code != 200:
        print("Error searching for track:", search_response.json())
        return []

    tracks = search_response.json()['tracks']['items']
    return tracks

# Function to get an artist's top tracks
def get_artist_top_tracks(artist_name):
    # Get the artist ID from the artist name
    artist_id = get_artist_id(artist_name)
    
    if not artist_id:
        return []
    
    # Get the artist's top tracks
    top_tracks = sp.artist_top_tracks(artist_id)
    track_names = [track['name'] for track in top_tracks['tracks']]
    
    print()
    print(f"Top Tracks for {artist_name}:")
    for index, name in enumerate(track_names, start=1):
        print(f"{index}. {name}")
    
    return track_names

def get_artist_id(artist_name):
    # Search for the artist by name
    results = sp.search(q=artist_name, type='artist', limit=1)
    artists = results.get('artists', {}).get('items', [])
    
    if not artists:
        print(f"No artist found for: {artist_name}")
        return None
    
    # Return the first artist's ID
    return artists[0]['id']




