"""
auth.py

This module handles authentication to the Spotify Web API
using spotipy and OAuth.

It provides a function to obtain an authenticated Spotify client
that can be used to access user-specific endpoints.

Environment variables required:
- SPOTIPY_CLIENT_ID
- SPOTIPY_CLIENT_SECRET
- SPOTIPY_REDIRECT_URI

Current scope:
- user-top-read (access to user's top artists and tracks)
"""

import os
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

def get_spotify_client():
    """
    Initializes and returns an authenticated Spotify client.

    Loads credentials from .env file, sets required OAuth scope,
    and uses Spotipy to manage token authentication.

    Returns:
        spotipy.Spotify: Authenticated Spotify client.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Define required Spotify OAuth scope
    scope = "user-top-read"

    # Return authenticated Spotify client
    return Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=scope,
    ))
