import unittest
from unittest.mock import patch, Mock
import sys
from io import StringIO
from my_module import *
from project import *

class TestSpotifyManager(unittest.TestCase):

    # **Test Access Token Retrieval**
    @patch('requests.post')
    def test_get_access_token(self, mock_post):
        # Mock the response from requests.post
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'access_token': 'mock_token'}
        mock_post.return_value = mock_response

        # Call the function
        token = get_access_token()

        # Assertions
        self.assertEqual(token, 'mock_token')
        mock_post.assert_called_once()

    # **Test User ID Retrieval**
    @patch('spotipy.Spotify')
    def test_get_user_id(self, mock_spotify):
        # Mock the Spotify object and its current_user method
        mock_sp = Mock()
        mock_sp.current_user.return_value = {'id': 'mock_user_id'}
        mock_spotify.return_value = mock_sp

        # Call the function
        user_id = get_user_id()

        # Assertions
        self.assertEqual(user_id, 'mock_user_id')


    @patch('spotipy.Spotify')
    def test_get_user_playlists(self, mock_spotify):
        # Mock the Spotify object and its current_user_playlists method
        mock_sp = Mock()
        mock_sp.current_user_playlists.return_value = {
            'items': [
                {'name': 'Playlist 1'},
                {'name': 'Playlist 2'},
                None  # Simulate a None value in the list
            ]
        }
        mock_spotify.return_value = mock_sp

        # Capture the output of the print statement
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function
        get_user_playlists()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Assertions
        expected_output = "Your Playlists:\n\n1. Playlist 1\n2. Playlist 2\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
        mock_sp.current_user_playlists.assert_called_once()


if __name__ == '__main__':
    unittest.main()