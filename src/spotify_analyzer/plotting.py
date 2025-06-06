"""
plotting.py

This module provides plotting functions for visualizing Spotify listening behavior.

All functions take DataFrames (as produced by analysis.py) and return Plotly Figures.
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from typing import Optional

# Optional: reusable bar plot utility
def _plot_horizontal_bar(df: pd.DataFrame, x: str, y: str, title: str, color_scale: str = "Viridis") -> go.Figure:
    fig = px.bar(
        df,
        x=x,
        y=y,
        orientation='h',
        title=title,
        color=x,
        color_continuous_scale=color_scale,
        template='plotly_white'
    )
    fig.update_layout(yaxis=dict(autorange="reversed"))
    return fig

# Plot top genres
def plot_top_genres(genres_df: pd.DataFrame, time_range: str) -> go.Figure:
    """
    Plots top genres for a given time range.

    Args:
        genres_df (pd.DataFrame): Output of get_top_genres.
        time_range (str): Time range string for plot title.

    Returns:
        plotly.graph_objects.Figure
    """
    return _plot_horizontal_bar(
        genres_df,
        x='count',
        y='genre',
        title=f"Top Genres ({time_range.replace('_', ' ').title()})"
    )

# Plot artist loyalty over time
def plot_artist_loyalty(loyalty_df: pd.DataFrame) -> go.Figure:
    """
    Plots artist loyalty over time.

    Args:
        loyalty_df (pd.DataFrame): Output of get_artist_loyalty.

    Returns:
        plotly.graph_objects.Figure
    """
    fig = px.bar(
        loyalty_df,
        x='time_range',
        y='unique_artists',
        title="Artist Loyalty Over Time",
        text_auto=True,
        color='unique_artists',
        color_continuous_scale='Blues',
        template='plotly_white'
    )
    return fig

# Plot genre diversity over time
def plot_genre_diversity(diversity_df: pd.DataFrame) -> go.Figure:
    """
    Plots genre diversity (entropy) over time.

    Args:
        diversity_df (pd.DataFrame): Output of get_genre_diversity.

    Returns:
        plotly.graph_objects.Figure
    """
    fig = px.bar(
        diversity_df,
        x='time_range',
        y='genre_entropy',
        title="Genre Diversity (Entropy) Over Time",
        text_auto='.2f',
        color='genre_entropy',
        color_continuous_scale='Purples',
        template='plotly_white'
    )
    return fig

# Plot average duration over time
def plot_average_duration(duration_df: pd.DataFrame) -> go.Figure:
    """
    Plots average track duration over time.

    Args:
        duration_df (pd.DataFrame): Output of get_average_duration.

    Returns:
        plotly.graph_objects.Figure
    """
    fig = px.bar(
        duration_df,
        x='time_range',
        y='avg_duration_min',
        title="Average Track Duration Over Time",
        text_auto='.2f',
        color='avg_duration_min',
        color_continuous_scale='Greens',
        template='plotly_white'
    )
    return fig

# Optional: radar chart of "personality"
def plot_personality_radar(personality_df: pd.DataFrame) -> go.Figure:
    """
    Plots a personality radar chart.

    Expected columns: ['metric', 'value']

    Args:
        personality_df (pd.DataFrame): Combined metrics.

    Returns:
        plotly.graph_objects.Figure
    """
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=personality_df['value'],
        theta=personality_df['metric'],
        fill='toself',
        name='Personality Profile'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True)
        ),
        showlegend=False,
        title="Listening Personality Radar"
    )

    return fig
