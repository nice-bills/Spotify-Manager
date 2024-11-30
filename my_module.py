import requests
import base64
import sys
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from project import add_track_to_playlist, remove_track_from_playlist 

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = 'http://localhost:5000/callback'
scope = "playlist-read-private user-read-private playlist-modify-public"

user_id = None

sp = spotipy.Spotify(auth_manager= SpotifyOAuth(client_id = client_id,client_secret = client_secret,redirect_uri = redirect_uri,scope = scope))


#this function allows for the user to get his token
def get_access_token():
    # Encode client ID and secret
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    # Request access token
    response = requests.post(
        'https://accounts.spotify.com/api/token',
        headers={
            'Authorization': f'Basic {encoded_credentials}',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data={'grant_type': 'client_credentials'}
    )

    if response.status_code != 200:
        print("Error getting access token:", response.json())
        sys.exit(1)
    global token
    token =response.json().get('access_token') 
    return token

# Function to get the user's Spotify ID
def get_user_id():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= client_id,client_secret= client_secret, redirect_uri= redirect_uri,scope= "user-read-private"))
    user_info = sp.current_user()
    global user_id
    user_id = user_info['id']
    return user_id

# # Function to create a playlist
# def create_playlist(name):
#     global user_id
#     if user_id is None:
#         get_user_id()  # Ensure user_id is set
#     playlist = sp.user_playlist_create(user=user_id, name= name, public=True)
#     print(f"Playlist '{name}' created successfully!")
#     # print(playlist["id"])
#     global playlist_id
#     playlist_id = playlist["id"]
#     return playlist_id


# Function to get user's playlists
def get_user_playlists():
    playlists = sp.current_user_playlists()
    return playlists["items"]



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
def get_artist_top_tracks(token, artist_name):
    search_url = f'https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=10'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    search_response = requests.get(search_url, headers=headers)

    if search_response.status_code != 200:
        print("Error searching for artist:", search_response.json())
        return []

    artists = search_response.json()['artists']['items']
    if not artists:
        print("No artist found.")
        return []

    artist_id = artists[0]['id']  # Get the first artist's ID
    top_tracks_url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=US'
    top_tracks_response = requests.get(top_tracks_url, headers=headers)

    if top_tracks_response.status_code != 200:
        print("Error getting top tracks:", top_tracks_response.json())
        return []

# Function to add or remove songs from a selected playlist
def manage_playlist_tracks(playlist_id):
    token = get_access_token()
    if not token:
        print("Failed to get access token.")
        return
    while True:
        print("\nManage Playlist Tracks:")
        print("1. Add Track to Playlist")
        print("2. Remove Track from Playlist")
        print("3. Return to Previous Menu")

        choice = input("Select an option: ")

        if choice == '1':
            track_name = input("Enter track name to add: ")
            tracks = search_track(token, track_name)
            if tracks:
                print("Select a track to add:\n")
                for index, track in enumerate(tracks):
                    print(f"{index + 1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
                track_index = int(input("Select track number: ")) - 1
                if 0 <= track_index < len(tracks):
                    add_track_to_playlist(playlist_id, [tracks[track_index]['uri']])
                else:
                    print("Invalid track selection.")
            else:
                print("No tracks found.")

        elif choice == '2':
            track_name = input("Enter track name to remove: ")
            tracks = search_track(token, track_name)
            if tracks:
                print("Select a track to remove:\n")
                for index, track in enumerate(tracks):
                    print(f"{index + 1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
                track_index = int(input("Select track number: ")) - 1
                if 0 <= track_index < len(tracks):
                    remove_track_from_playlist(playlist_id, [tracks[track_index]['uri']])
                else:
                    print("Invalid track selection.")
            else:
                print("No tracks found.")

        elif choice == '3':
            break

        else:
            print("Invalid option. Please try again.")
            
