import unittest
from unittest.mock import patch, Mock
import sys
from io import StringIO
from my_module import *
from project import *

class TestSpotifyManager(unittest.TestCase):

    @patch('requests.post')
    def test_get_access_token(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'access_token': 'mock_token'}
        mock_post.return_value = mock_response

        token = get_access_token()

        self.assertEqual(token, 'mock_token')
        mock_post.assert_called_once()

class TestSpotifyManager(unittest.TestCase):

    @patch('spotipy.Spotify')
    def test_get_user_id(self, mock_spotify):
        mock_sp = Mock()
        mock_sp.current_user.return_value = {'id': 'mock_user_id'}
        mock_spotify.return_value = mock_sp

        user_id = get_user_id()

        self.assertEqual(user_id, 'mock_user_id')


class TestSpotifyUserPlaylists(unittest.TestCase):

    @patch('spotipy.Spotify.current_user_playlists')
    def test_get_user_playlists_success(self, mock_current_user_playlists):
        mock_current_user_playlists.return_value = {
            "items": [
                {
                    "id": "playlist_id_1",
                    "name": "My Favorite Songs",
                    "owner": {
                        "display_name": "User  Name"
                    }
                },
                {
                    "id": "playlist_id_2",
                    "name": "Chill Vibes",
                    "owner": {
                        "display_name": "User  Name"
                    }
                }
            ]
        }
        
        access_token = "valid_access_token"
        
        playlists = TestFunctions.test_get_user_playlists(access_token)
        
        self.assertEqual(len(playlists), 2)
        self.assertEqual(playlists[0]['name'], "My Favorite Songs")
        self.assertEqual(playlists[1]['name'], "Chill Vibes")
        mock_current_user_playlists.assert_called_once()
        
        
        
class TestSpotifySongSearch(unittest.TestCase):

    @patch('spotipy.Spotify.search')
    def test_search_songs_success(self, mock_search):
        mock_search.return_value = {
            "tracks": {
                "items": [
                    {
                        "id": "track_id_1",
                        "name": "Song One",
                        "artists": [{"name": "Artist One"}],

                    },
                    {
                        "id": "track_id_2",
                        "name": "Song Two",
                        "artists": [{"name": "Artist Two"}],
                    }
                ]
            }
        }
        
        access_token = "valid_access_token"
        query = "test song"
        
        songs = TestFunctions.test_search_songs(query, access_token)
        
        self.assertEqual(len(songs), 2)
        self.assertEqual(songs[0]['name'], "Song One")
        self.assertEqual(songs[1]['name'], "Song Two")
        mock_search.assert_called_once_with(q=query, type='track', limit=10)


class TestSpotifyArtistTracks(unittest.TestCase):

    @patch('spotipy.Spotify.artist_albums')
    @patch('spotipy.Spotify.album_tracks')
    def test_get_artist_tracks_success(self, mock_album_tracks, mock_artist_albums):
        mock_artist_albums.return_value = {
            "items": [
                {"id": "album_id_1"},
                {"id": "album_id_2"}
            ]
        }
        
        mock_album_tracks.side_effect = [
            {
                "items": [
                    {"id": "track_id_1", "name": "Track One" },
                    {"id": "track_id_2", "name": "Track Two"}
                ]
            },
            {
                "items": [
                    {"id": "track_id_3", "name": "Track Three"}
                ]
            }
        ]
        
        access_token = "valid_access_token"
        artist_id = "artist_id"
        
        tracks = TestFunctions.test_get_artist_tracks(artist_id, access_token)
        
        self.assertEqual(len(tracks), 3)
        self.assertEqual(tracks[0]['name'], "Track One")
        self.assertEqual(tracks[1]['name'], "Track Two")
        self.assertEqual(tracks[2]['name'], "Track Three")
        mock_artist_albums.assert_called_once_with(artist_id, album_type='album')
        self.assertEqual(mock_album_tracks.call_count, 2)

if __name__ == '__main__':
    unittest.main()