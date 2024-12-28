# Spotify Manager

## Overview

#### Video Demo

**Spotify Manager** is a Python application that allows users to interact with the Spotify API to manage their music experience. This application provides functionalities such as searching for tracks, retrieving an artist's top songs, and displaying the user's playlists. It utilizes the Spotipy library for seamless interaction with the Spotify Web API and leverages OAuth for secure authentication.

## Table Of Contents

- [Features](#features)

- [Installation](#installation)

- [Usage](#usage)

- [Authentication](#authentication)

- [Functions Overview](#functions-overview)

- [Contributing](#contributing)

### Features

- **Display User Playlists**: The application fetches and displays the user's created playlists, providing a quick overview of their music collections.

- **Search For Tracks**: Users can search for their favorite tracks by entering the track name. The application will return a list of matching tracks along with their artists.

- **Get Artist's Top Songs**: Users can input an artist's name to retrieve their top tracks, allowing for easy access to popular songs.

- **Secure Authentication**: The application uses OAuth 2.0 for secure access to the Spotify API, ensuring that user credentials are handled safely.

- **User-Friendly Interface**: The application is designed with a simple command-line interface, making it easy for users to navigate and use its features.

### Installation

To get started with the Spotify Manager, you would need to follow these steps:

1.  **Download the Project**:

    - Download the project files from the source where you obtained them and extract them to a directory of your choice.

2.  **Install Dependencies**:

    - Make sure you have Python installed on your system. You can download the latest version from the official Python website. Then, install the required packages using `pip`

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Up Environment Variables**:

    - Create a `.env` file in the root of your project directory and add your Spotify API credentials:

    ```python
    CLIENT_ID = your_client_id
    CLIENT_SECRET = your_client_secret
    ```

### Usage

To run the application, execute the following command in your terminal:

```bash
python project.py
```

Once the application is running, you will be presented with a main menu where you can choose from the following options:

1.  **Search for a Track**: Enter the name of the track you would like to search for.

2.  **Get Artist's Top Songs**: Enter the name of the artist you would like to retrieve top songs for.

3.  **Display Your Created Playlists**: View all playlists you have created on Spotify.

4.  **Exit**: Quit the application.

### Authentication

The Spotify Manager uses OAuth 2.0 for secure authentication. The application requires a valid `CLIENT_ID` and `CLIENT_SECRET` from the Spotify Developer Dashboard. Follow these steps to obtain your credentials:

1.  Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

2.  Log in or create an account.

3.  Create a new application to get your `CLIENT_ID` and `CLIENT_SECRET`.

4.  Set the `redirect_uri` to `http://localhost:5000/callback` in the Spotify Developer Dashboard.

### Functions Overview

The main functionalities of the application are found in several key functions:

- **get_access_token()**: This function retrieves an access token from the Spotify API using the provided `CLIENT_ID` and `CLIENT_SECRET`.

- **get_user_id()**: This function gets the user's ID from the Spotify API using the access token.

- **get_user_playlists()**: This function retrieves the user's created playlists from the Spotify API using the access token and user ID.

- **main()**: This is the main function that handles user input and calls the necessary functions to perform the desired actions.

### Contributing

Contributions are welcome! If you would like to contribute to the Spotify Manager project, please follow these steps:

1. Identify the feature or bug you would like to work on.

2. Make your changes and ensure they are well-tested.

3. Document your changes clearly.
# Spotify-Manager
