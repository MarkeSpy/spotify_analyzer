# Spotify Listening Analyzer

An interactive data app that analyzes your Spotify listening behavior using the Spotify Web API.

Built with:

- Python 3.12+
- Spotipy (for API access)
- Pandas (for data analysis)
- Plotly (for interactive visualizations)
- Streamlit (for the web app UI)

---

## Features (MVP)

✅ Analyze top 50 tracks per Spotify time range:

- `short_term` (4 weeks)
- `medium_term` (6 months)
- `long_term` (all time)

### Metrics:

- 🎵 Top Genres (with evolution over time)
- 🎧 Artist Loyalty (unique artists per timeframe)
- 🌎 Genre Diversity (entropy measure)

---

## Project Structure

```plaintext
spotify_analyzer/
|├️ notebooks/
|   └️ analysis.ipynb  # Exploration and testing
|├️ src/
    └️ spotify_analyzer/
        |├️ __init__.py
        |├️ auth.py         # Spotify authentication
        |├️ data.py         # Data loading (top tracks, artist genres)
        |├️ analysis.py     # Analysis functions
        |└️ plotting.py     # Plotting functions
|├️ app.py                # Streamlit app entry point
|├️ main.py               # (optional) CLI entry point
|├️ .env                  # Environment variables (not committed)
|└️ .gitignore
```

## How to Run

1. Clone the repo:

```bash
git clone https://github.com/yourusername/spotify_analyzer.git
cd spotify_analyzer
```
2. Create and activate a virtual environment:
   
```bash
conda create -n spotify_project python=3.12
conda activate spotify_project
```
3. Install dependencies:

```bash
pip install -r requirements.txt
```
4. Set up `.env` file:
```plaintext
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8080

```
5. Run Streamlit app:
```bash
streamlit run app.py
```

##  Current Limitations
- Only retrieves top 50 tracks per time range due to Spotify API limits.
- Limited data scope (“user-top-read” scope only).
- Only analyzes your own listening data (not global trends).

## Future Improvements
- 🔍 Broaden data scope (recently played, playlists, saved tracks)

- 📊 Historical tracking (store data over time)

- 🔄 Scheduled runs / data caching

- 🔧 Deployment as public app (Heroku / Streamlit Cloud)

- 👤 Multi-user support (OAuth login)

- 🌍 Comparative dashboards

## License
MIT License.




