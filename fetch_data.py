import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pyyoutube import Api as YouTubeApi
from datetime import datetime

# Replace with your credentials
SPOTIFY_CLIENT_ID = "6e7e4b94f2004db982218c63dd735a74"
SPOTIFY_CLIENT_SECRET = "ed0ff44ae35e4f8ab1d8e8aa582dc983"
YOUTUBE_API_KEY = "AIzaSyCMW_qzBL0kVtnzc6me06Nz90UUW8Qitdk"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))
yt = YouTubeApi(api_key=YOUTUBE_API_KEY)

def fetch_tiktok_data(genre):
    return {"clips": "300% increase this week"}  # Mock until API

def fetch_x_data(genre):
    return {"mentions": "up 300% this week", "top_phrase": "the soundtrack to every perfect day"}  # Mock until API

def fetch_data(genre):
    playlist_map = {
        "Indie Pop": "37i9dQZF1DX2L0iB23Enbq",  # Indie Rising
        "Country": "37i9dQZF1DX1lVhptIYRda",    # Hot Country
        "Hip-Hop": "37i9dQZF1DX0XUsuxWHRQd",  # RapCaviar
        "Rock": "37i9dQZF1DXcF6B6QCTT9T",     # Rock This
        "Folk": "37i9dQZF1DX9HwI3CrikLt"      # Folk & Friends
    }
    playlist_id = playlist_map.get(genre, "37i9dQZF1DX2L0iB23Enbq")

    try:
        results = sp.playlist_tracks(playlist_id)
        track = results["items"][0]["track"]
        streams = track["popularity"] * 10000
        likes = int(streams * 0.06)
        platform_highlight = f"Spotify: #{results['items'].index(track) + 1} on {genre} playlist"

        yt_search = yt.search_by_keywords(q=f"{track['name']} {track['artists'][0]['name']}", search_type=["video"], count=1)
        yt_video = yt_search.items[0] if yt_search.items else None
        yt_buzz = f"YouTube: {yt_video.view_count if yt_video else 'N/A'} views" if yt_video else "YouTube: Trending soon"

        tiktok_data = fetch_tiktok_data(genre)
        x_data = fetch_x_data(genre)

        return {
            "track_title": track["name"],
            "artist": track["artists"][0]["name"],
            "platform_highlights": platform_highlight,
            "engagement_metrics": f"{streams} streams, {likes} likes",
            "buzz": f"A {genre.lower()} gem—{x_data['top_phrase']}, {x_data['mentions']}",
            "tiktok_clips": tiktok_data["clips"]
        }
    except Exception as e:
        return {
            "track_title": "Fallback Track",
            "artist": "Unknown",
            "platform_highlights": "Spotify: TBD",
            "engagement_metrics": "100K streams, 5K likes",
            "buzz": f"A {genre.lower()} placeholder—awaiting data",
            "tiktok_clips": "N/A"
        }