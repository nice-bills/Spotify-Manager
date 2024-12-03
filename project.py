# import the necessary functions 
from my_module import *
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = 'http://localhost:5000/callback'
scope ="playlist-read-private user-read-private playlist-modify-public playlist-modify-private user-library-read"

sp = spotipy.Spotify(auth_manager= SpotifyOAuth(client_id = client_id,client_secret = client_secret,redirect_uri = redirect_uri,scope = scope))

def get_user_playlists():
    user_tracks = sp.current_user_playlists()
    playlists = [item for item in user_tracks['items'] if item is not None]

    print("Your Playlists:\n")
    for index, playlist in enumerate(playlists, start=1):
        print(f"{index}. {playlist['name']}")

# Main function to run the Spotify Manager
def main():
    token = get_access_token()
    if not token:
        print("Failed to get access token.")
        return
    while True:
        print("\nMain Menu:")
        print("1. Search for a Track")
        print("2. Get Artist's Top Songs")
        print("3. Display your created playlist")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            track_name = input("Enter track name to search: ")
            tracks = search_track(token, track_name)
            if tracks:
                print("Search Results:\n")
                for index, track in enumerate(tracks):
                    print(f"{index + 1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
            else:
                print("No tracks found.")

        elif choice == '2':
            artist_name = input("Enter your artist's name: ")
            get_artist_top_tracks(artist_name)
        
        elif choice == '3':
            get_user_playlists()
            
        elif choice == '4':
            print("Exiting the application.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()