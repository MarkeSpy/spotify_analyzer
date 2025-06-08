"""
My first app
"""
import streamlit as st
st.set_page_config(page_title="Spotify Listening Analyzer", layout="wide")
import pandas as pd
import sys
import os

# Add src to path
sys.path.append(os.path.abspath("./src"))

# Explicit imports — cleaner, safer
from spotify_analyzer.data import *
from spotify_analyzer.analysis import *
from spotify_analyzer.plotting import plot_top_genres

# Sidebar - time range selection
st.sidebar.title("Spotify Analyzer")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["short_term", "medium_term", "long_term",None]
)

# Sidebar - top N
top_n = st.sidebar.slider("Top N Genres", min_value=5, max_value=20, value=10)

# Main app
st.title("🎵 Spotify Listening Analyzer")

evolution = st.sidebar.checkbox("Show Evolution Over Time", value=False)

if evolution:
    st.sidebar.write("Evolution mode active → no time range needed")
    st.info("Loading data from Spotify...")
    df = get_all_time_ranges()
    df = enrich_with_genres(df)
    genres_df = get_top_genres(df, evolution=True, top_n=top_n)
    fig_genres = plot_top_genres(genres_df, evolution=True)
    st.plotly_chart(fig_genres, use_container_width=True)

else:
    time_range = st.sidebar.selectbox(
        "Select Time Range",
        options=["short_term", "medium_term", "long_term"],
        index=0
    )
    st.info("Loading data from Spotify...")
    df = get_top_tracks(time_range)
    df = enrich_with_genres(df)
    genres_df = get_top_genres(df, time_range=time_range, top_n=top_n)
    fig_genres = plot_top_genres(genres_df, time_range=time_range)
    st.plotly_chart(fig_genres, use_container_width=True)


# Show raw data (optional debug)
with st.expander("Show Raw DataFrame"):
    st.dataframe(df)
