# import the necessary functions 
from my_module import *
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = 'http://localhost:5000/callback'
scope = "playlist-read-private user-read-private playlist-modify-public"

sp = spotipy.Spotify(auth_manager= SpotifyOAuth(client_id = client_id,client_secret = client_secret,redirect_uri = redirect_uri,scope = scope))

# Function to create a playlist
def create_playlist(name):
    global user_id
    if user_id is None:
        get_user_id()  # Ensure user_id is set
    playlist = sp.user_playlist_create(user=user_id, name= name, public=True)
    print(f"Playlist '{name}' created successfully!")
    # print(playlist["id"])
    global playlist_id
    playlist_id = playlist["id"]
    return playlist_id

# # Function to get user's playlists
# def get_user_playlists():
#     playlists = sp.current_user_playlists()
#     return playlists["items"]

#Enables the addition of songs to a playlist
def add_track_to_playlist(playlist_id, track_uri):
    sp.playlist_add_items(playlist_id=playlist_id, items=track_uri)
    print(f"'{track_name}' has been added to playlist successfully!")
    
# Function to remove a track from a playlist
def remove_track_from_playlist(playlist_id, track_uri):
    sp.playlist_remove_all_occurrences_of_items(playlist_id=playlist_id, items=track_uri)
    print(f"'{track_name}' has been removed from playlist successfully!")

# Main function to run the Spotify Playlist Manager
def main():
    token = get_access_token()
    if not token:
        print("Failed to get access token.")
        return
    while True:
        print("\nMain Menu:")
        print("1. Create Playlist")
        print("2. Get User Playlists")
        print("3. Search for a Track")
        print("4. Get Artist's Top Songs")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter playlist name: ")
            playlist = create_playlist(name)

            if playlist:
                # Nested menu for adding/removing tracks
                while True:
                    print("\nPlaylist Menu:")
                    print("1. Add Track to Playlist")
                    print("2. Remove Track from Playlist")
                    print("3. Return to Main Menu")

                    playlist_choice = input("Select an option: ")

                    if playlist_choice == '1':
                        global track_name
                        track_name = input("Enter track name to add: ")
                        tracks = search_track(token, track_name)
                        if tracks:
                            print("Select a track to add:\n")
                            for index, track in enumerate(tracks):
                                print(f"{index + 1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
                            track_index = int(input("Select track number: ")) - 1
                            if 0 <= track_index < len(tracks):
                                add_track_to_playlist(playlist_id, [tracks[track_index]['uri']])
                                print(f"'{track_name}' has been added to playlist successfully!")
                            else:
                                print("Invalid track selection.")
                        else:
                            print("No tracks found.")

                    elif playlist_choice == '2':
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

                    elif playlist_choice == '3':
                        break

                    else:
                        print("Invalid option. Please try again.")

        elif choice == '2':
            playlists = get_user_playlists()
            if playlists:
                print("Your Playlists:\n")
                for index, playlist in enumerate(playlists):
                    print(f"{index + 1}. {playlist['name']}")
                playlist_index = int(input("Select a playlist to manage: ")) - 1
                if 0 <= playlist_index < len(playlists):
                    selected_playlist_id = playlists[playlist_index]['id']
                    manage_playlist_tracks(selected_playlist_id)
                else:
                    print("Invalid playlist selection.")
            else:
                print("No playlists found.")

        elif choice == '3':
            track_name = input("Enter track name to search: ")
            tracks = search_track(token, track_name)
            if tracks:
                print("Search Results:\n")
                for index, track in enumerate(tracks):
                    print(f"{index + 1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
            else:
                print("No tracks found.")

        elif choice == '4':
            artist_name = input("Enter artist name to search for top songs: ")
            top_tracks = get_artist_top_tracks(token, artist_name)
            if top_tracks:
                print(f"Top Songs for {artist_name}:\n")
                for index, track in enumerate(top_tracks):
                    print(f"{index + 1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
            else:
                print("No top songs found for this artist.")

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()