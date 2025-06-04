import pandas as pd
from spotify_analyzer.auth import get_spotify_client

### AUTHENTICATE ###
sp = get_spotify_client()

def get_top_tracks(time_range,limit=50):
    results = sp.current_user_top_tracks(time_range=time_range,limit=limit)

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

def get_all_time_ranges():
    dfs = []
    for time_range in ['short_term','medium_term','long_term']:
        df = get_top_tracks(time_range)
        dfs.append(df)
    return pd.concat(dfs,ignore_index=True)
        

def get_artist_genres(artist_ids):
    genres = {}
    for artist_id in artist_ids:
        artist = sp.artist(artist_id)
        genres[artist_id] = artist.get('genres', [])
    return genres

def enrich_with_genres(df):
    artist_ids = df['artist_id'].unique()
    genre_map = get_artist_genres(artist_ids)
    df['genres'] = df['artist_id'].map(lambda x: genre_map.get(x, []))
    return df