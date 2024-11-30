# playlist_manager.py

class PlaylistManager:
    def __init__(self):
        self.playlist_dict = {}

    def add_track(self, artist_name, track_name):
        if artist_name not in self.playlist_dict:
            self.playlist_dict[artist_name] = []
        self.playlist_dict[artist_name].append(track_name)

    def remove_track(self, artist_name, track_name):
        if artist_name in self.playlist_dict:
            if track_name in self.playlist_dict[artist_name]:
                self.playlist_dict[artist_name].remove(track_name)
                if not self.playlist_dict[artist_name]:  # Remove artist if no songs left
                    del self.playlist_dict[artist_name]

    def get_playlist(self):
        return self.playlist_dict

    def display_playlist(self):
        for artist, songs in self.playlist_dict.items():
            print(f"{artist}: {', '.join(songs)}")