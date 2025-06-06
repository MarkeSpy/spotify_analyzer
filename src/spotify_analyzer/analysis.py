"""
analysis.py

This module provides analysis functions for Spotify listening behavior.

All functions take as input a DataFrame of enriched track data (with genres),
and return DataFrames or scalar values representing various user behavior metrics.

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
from typing import Optional

def get_top_genres(df: pd.DataFrame, time_range: str, top_n: Optional[int] = None) -> pd.DataFrame:
    """
    Returns top genres for a given time range.

    Args:
        df (pd.DataFrame): Enriched tracks DataFrame.
        time_range (str): One of 'short_term', 'medium_term', 'long_term'.
        top_n (int, optional): Number of top genres to return.

    Returns:
        pd.DataFrame: Columns ['genre', 'count'].
    """
    pass

def get_artist_loyalty(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes artist loyalty: number of unique artists per time range.

    Args:
        df (pd.DataFrame): Enriched tracks DataFrame.

    Returns:
        pd.DataFrame: Columns ['time_range', 'unique_artists'].
    """
    pass

def get_genre_diversity(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes genre diversity (entropy) per time range.

    Args:
        df (pd.DataFrame): Enriched tracks DataFrame.

    Returns:
        pd.DataFrame: Columns ['time_range', 'genre_entropy'].
    """
    pass

def get_average_duration(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes average track duration per time range (in minutes).

    Args:
        df (pd.DataFrame): Enriched tracks DataFrame.

    Returns:
        pd.DataFrame: Columns ['time_range', 'avg_duration_min'].
    """
    pass
