import pytest
from my_module import *
from project import get_user_playlists

def main():
    test_artist_top_tracks()
    test_get_user_playlist()
    test_get_access_token()
    test_search_track()
    test_get_user_id()
    
def test_get_access_token():
    ...
    
def test_get_user_id():
    ...

def test_get_user_playlist():
    ...
    
def test_search_track():
    ...
    
def test_artist_top_tracks():
    ...


if __name__ == "__main__":
    main()