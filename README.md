# Spotify Playlist Management

## Overview

The Spotify Playlist Management application is a powerful tool that allows users to efficiently manage their Spotify playlists through a user-friendly command-line interface. Built using the `spotipy` library, this application enables users to create new playlists, view existing playlists, and add or remove tracks with ease. Whether you're a casual listener or a music enthusiast, this application provides the necessary features to enhance your Spotify experience.

## Features

- **Create Playlist**: Users can create a new playlist directly in their Spotify account by simply providing a name for the playlist. This feature allows for personalized music organization tailored to any occasion or mood.

- **View Playlists**: The application retrieves and displays all playlists associated with the user's Spotify account. This feature makes it easy to manage and select playlists for further actions.

- **Manage Tracks**: Users can add or remove tracks from any selected playlist. The application allows for easy searching of tracks by name, providing a list of matching results for users to choose from.

- **Search Tracks**: The application includes a robust search function that enables users to find specific tracks by name.

- **Artiste Search**: Users can search for artists by name and view their top tracks.

## Prerequisites

Before running the application, ensure that you have the following:

- **Python 3.x**: The application is built with Python, so you need to have Python installed on your machine.
- **Spotify Developer Account**: Sign up for a Spotify Developer account to access the Spotify API.
- **Spotify API Credentials**: Obtain your Client ID, Client Secret, and Redirect URI from the Spotify Developer Dashboard.
- **Required Libraries**: The application requires the `spotipy`, `request` and `python-dotenv` libraries.

## Installation

To get started with the Spotify Playlist Management application, follow these steps:

1. **Clone the Repository**:

```bash
git clone https://github.com/yourusername/spotify-playlist-management.git
cd spotify-playlist-management
```

2. **Install Required Libraries**:

```bash
pip install -r requirements.txt
```

3. **Create a `.env` File from the .env.sample file**:

```
cp .env.sample .env
```
