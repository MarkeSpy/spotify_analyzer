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
def _plot_bar(
    df: pd.DataFrame,
    evolution: bool,
    x: str,
    y: str,
    title: str,
    color: str,
    orientation: str = 'v'
) -> go.Figure:
    if evolution:
        # Evolution → grouped vertical bar chart
        fig = px.bar(
            df,
            x=x,
            y=y,
            color=color,
            barmode='group',
            title=title,
            template='plotly_white'
        )
    else:
        # Single time range → horizontal bar
        fig = px.bar(
            df,
            x=x,
            y=y,
            orientation=orientation,
            color=color,
            color_continuous_scale="Viridis",
            title=title,
            template='plotly_white'
        )
        # Only reverse axis for horizontal
        if orientation == 'h':
            fig.update_layout(yaxis=dict(autorange="reversed"))

    return fig


# Plot top genres
def plot_top_genres(
    df: pd.DataFrame,
    time_range: Optional[str] = None,
    evolution: bool = False
) -> go.Figure:
    """
    Plots top genres for a given time range.

    Args:
        genres_df (pd.DataFrame): Output of get_top_genres.
        time_range (str): Time range string for plot title.

    Returns:
        plotly.graph_objects.Figure
    """
    if evolution and time_range is not None:
        raise ValueError("Cannot specify both evolution=True and time_range. Choose one.")

    if evolution:
        return _plot_bar(
            df,
            evolution=evolution,
            x='genre',
            y='count',
            color='time_range',
            title=f'Top Genre Frequency Across Time Ranges'
    )
    if not time_range:
        raise ValueError("You must specify time_range when evolution=False")
    
    return _plot_bar(df,evolution=evolution, x='count',y='genre',title=f"Top Genres ({time_range.replace('_', ' ').title()})", color='count', orientation='h')

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
