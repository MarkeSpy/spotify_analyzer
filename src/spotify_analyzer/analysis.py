"""
analysis.py

This module provides analysis functions for Spotify listening behavior.

All functions take as input a DataFrame of enriched track data (with genres),
and return DataFrames representing user behavior metrics.

Expected input DataFrame columns:
- name
- artist
- artist_id
- track_id
- duration_ms
- time_range
- genres (list of genres)
"""

import pandas as pd
from collections import Counter
from scipy.stats import entropy
from typing import Optional, List
import streamlit as st
# ---------- Top Genres ----------
def get_top_genres(
    df: pd.DataFrame,
    time_range: Optional[str] = None,
    top_n: Optional[int] = None,
    evolution: bool = False
) -> pd.DataFrame:
    """
    Returns top genres, either for one time range or across all time ranges.

    Returns:
        pd.DataFrame: Columns ['genre', 'count']
    """


    if evolution and time_range is not None:
        raise ValueError("Cannot specify both evolution=True and time_range. Choose one.")

    if evolution:
        result = []
        for tr in df['time_range'].unique():
            temp = get_top_genres(df, time_range=tr, top_n=top_n, evolution=False)
            result.append(temp)
        return pd.concat(result, ignore_index=True)

    if not time_range:
        raise ValueError("You must specify time_range when evolution=False")

    filtered_df = df.loc[df['time_range'] == time_range]
    genre_counts = Counter(genre for sublist in filtered_df['genres'] for genre in sublist)
    items = genre_counts.most_common(top_n) if top_n else genre_counts.items()
    return pd.DataFrame(items, columns=['genre', 'count']).assign(time_range = time_range)

# ---------- Artist Loyalty ----------
def get_artist_loyalty(
    df: pd.DataFrame,
    time_range: Optional[str] = None,
    evolution: bool = False
) -> pd.DataFrame:
    """
    Computes artist loyalty metrics:
    - unique_artists
    - loyalty_ratio
    - top_artist_dominance
    Returns:
        pd.DataFrame: Columns ['time_range', 'unique_artists', 'loyalty_ratio']
    """
    if evolution and time_range is not None:
        raise ValueError("Cannot specify both evolution=True and time_range. Choose one.")
    
    if evolution:
        result = []
        for tr in df['time_range'].unique():
            temp = get_artist_loyalty(df, time_range=tr, evolution=False)
            result.append(temp)
        return pd.concat(result, ignore_index=True)

    if not time_range:
        raise ValueError("You must specify time_range when evolution=False")

    filtered_df = df.loc[df['time_range'] == time_range]
    
    unique_artists = filtered_df['artist'].nunique()
    loyalty_ratio = 1 - (unique_artists / len(filtered_df))
    
    return pd.DataFrame([{
        'time_range': time_range,
        'unique_artists': unique_artists,
        'loyalty_ratio': loyalty_ratio,
    }])


# ---------- Genre Diversity ----------
def get_genre_diversity(
    df: pd.DataFrame,
    time_range: Optional[str] = None,
    evolution: bool = False
) -> pd.DataFrame:
    """
    Computes genre diversity (entropy).

    Returns:
        pd.DataFrame: Columns ['time_range', 'genre_entropy']
    """
    if evolution and time_range is not None:
        raise ValueError("Cannot specify both evolution=True and time_range. Choose one.")
    
    def compute_entropy(genres_list: List[str]) -> float:
        counts = Counter(genres_list)
        probs = [count / sum(counts.values()) for count in counts.values()]
        return entropy(probs)

    if evolution:
        result = []
        for tr in df['time_range'].unique():
            temp = get_genre_diversity(df, time_range=tr, evolution=False)
            result.append(temp)
        return pd.concat(result, ignore_index=True)

    if not time_range:
        raise ValueError("You must specify time_range when evolution=False")

    filtered_df = df.loc[df['time_range'] == time_range]
    all_genres = [genre for sublist in filtered_df['genres'] for genre in sublist]
    diversity = compute_entropy(all_genres)
    return pd.DataFrame([{'time_range': time_range, 'genre_entropy': diversity}])

# ---------- Similarity Between Time Ranges (optional future feature) ----------
def get_genre_similarity(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes pairwise Jaccard similarity between genre sets of different time ranges.

    Returns:
        pd.DataFrame: Columns ['time_range_1', 'time_range_2', 'similarity']
    """
    # TODO: implement similarity logic
    pass

# ---------- Personality Profile (for radar chart) ----------
def get_personality_profile(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates key metrics for radar chart personality profile.

    Returns:
        pd.DataFrame: Columns ['metric', 'value']
    """
    # Example: you could combine genre diversity, loyalty, avg duration
    # TODO: implement personality profile logic
    pass

# ---------- Archetype Badge ----------
def get_listening_archetype(df: pd.DataFrame) -> str:
    """
    Returns a simple string badge describing user's listening archetype.

    Example return values:
    - 'Explorer'
    - 'Loyalist'
    - 'Mainstream Fan'
    - 'Underground Head'

    Returns:
        str
    """
    # TODO: implement archetype logic based on metrics
    pass