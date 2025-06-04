import plotly.express as px

def plot_top_genres(df, time_range):
    fig = px.bar(
        df,
        x='count',
        y='genre',
        orientation='h',
        title=f"Top Genres ({time_range.replace('_', ' ').title()})",
        color='count',
        color_continuous_scale='Viridis',
        template='plotly_white'
    )
    fig.update_layout(yaxis=dict(autorange="reversed"))
    return fig

def plot_top_artists(df, time_range):
    fig = px.bar(
        df,
        x='artist',
        y='count',
        title=f"Top Artists ({time_range.replace('_', ' ').title()})",
        color='count',
        color_continuous_scale='Blues',
        template='plotly_white'
    )
    return fig

def plot_avg_duration(df):
    fig = px.bar(
        df,
        x='time_range',
        y='duration_min',
        title="Average Track Duration by Time Range",
        text_auto='.2f',
        color='duration_min',
        color_continuous_scale='Purples',
        template='plotly_white'
    )
    return fig
