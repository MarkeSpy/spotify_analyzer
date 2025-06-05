"""
data.py

This module handles data collection from the Spotify Web API.

Provides functions to:
- Retrieve user's top tracks for a given time range
- Retrieve user's top tracks for all available time ranges
- Enrich tracks with artist genre information
"""

import pandas as pd
from typing import List, Dict
from spotify_analyzer.auth import get_spotify_client

# Initialize Spotify client (authenticated)
sp = get_spotify_client()

def get_top_tracks(time_range: str, limit: int = 50) -> pd.DataFrame:
    """
    Fetches the user's top tracks for a given time range.

    Args:
        time_range (str): One of 'short_term', 'medium_term', 'long_term'.
        limit (int, optional): Max number of tracks to retrieve (default is 50).

    Returns:
        pd.DataFrame: DataFrame containing track metadata:
            - name
            - artist
            - artist_id
            - track_id
            - popularity
            - duration_ms
            - time_range
    """
    results = sp.current_user_top_tracks(time_range=time_range, limit=limit)

    tracks = []
    for item in results['items']:
        track_info = {
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'artist_id': item['artists'][0]['id'],
            'track_id': item['id'],
            'popularity': item['popularity'],
            'duration_ms': item['duration_ms'],
            'time_range': time_range
        }
        tracks.append(track_info)

    df = pd.DataFrame(tracks)
    return df

def get_all_time_ranges() -> pd.DataFrame:
    """
    Fetches user's top tracks across all time ranges:
    - short_term
    - medium_term
    - long_term

    Returns:
        pd.DataFrame: Combined DataFrame of top tracks across all time ranges.
    """
    dfs = []
    for time_range in ['short_term', 'medium_term', 'long_term']:
        df = get_top_tracks(time_range)
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def get_artist_genres(artist_ids: List[str]) -> Dict[str, List[str]]:
    """
    Fetches genre information for a list of artist IDs.

    Args:
        artist_ids (List[str]): List of Spotify artist IDs.

    Returns:
        Dict[str, List[str]]: Mapping of artist_id -> list of genres.
    """
    genres = {}
    for artist_id in artist_ids:
        artist = sp.artist(artist_id)
        genres[artist_id] = artist.get('genres', [])
    return genres

def enrich_with_genres(df: pd.DataFrame) -> pd.DataFrame:
    """
    Enriches a DataFrame of tracks with genre information for each artist.

    Args:
        df (pd.DataFrame): DataFrame containing at least 'artist_id' column.

    Returns:
        pd.DataFrame: Same DataFrame with an added 'genres' column (list of genres per track).
    """
    artist_ids = df['artist_id'].unique()
    genre_map = get_artist_genres(artist_ids.tolist())
    df['genres'] = df['artist_id'].map(lambda x: genre_map.get(x, []))
    return df

def lela(time_range: str, limit: int = 50):
    results = sp.current_user_top_tracks(time_range=time_range, limit=limit)


    return results