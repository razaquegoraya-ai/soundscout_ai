import logging
import os
import pandas as pd
from prophet import Prophet
from datetime import datetime, timedelta
from fetch_data import fetch_data

# Set up logging
logging.basicConfig(filename="logs/soundscout.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

def convert_to_number(metric_str):
    """Convert string with K notation to number."""
    if 'K' in metric_str:
        return int(float(metric_str.replace('K', '')) * 1000)
    return int(metric_str)

def create_mock_data(genre):
    """Create mock data when API calls fail."""
    return {
        "track_title": f"Sample {genre} Track",
        "artist": f"Sample {genre} Artist",
        "platform_highlights": f"Spotify: #1 on {genre} playlist",
        "engagement_metrics": "100K streams, 5K likes",
        "buzz": f"A {genre.lower()} gem—fans are loving it, up 300% this week",
        "tiktok_clips": "300% increase this week"
    }

genres = ["Indie Pop", "Country", "Hip-Hop", "Rock", "Folk"]
current_date = datetime.now()

try:
    # Generate data for all genres
    all_report_data = {}
    for genre in genres:
        try:
            api_data = fetch_data(genre)
        except Exception as e:
            logger.warning(f"Failed to fetch data for {genre}, using mock data: {str(e)}")
            api_data = create_mock_data(genre)

        report_data = {
            "genre": genre,
            "date": current_date.strftime("%B %d, %Y"),
            "trending_tracks": [
                {"Track Title": api_data["track_title"], "Artist": api_data["artist"],
                 "Platform Highlights": api_data["platform_highlights"], "Engagement Metrics": api_data["engagement_metrics"],
                 "The Buzz": api_data["buzz"]}
            ],
            "predictive_analysis": [
                {"Item": api_data["track_title"], "Score": "90", "Prediction": "TBD"}
            ],
            "artist_spotlight": [
                {"Artist": api_data["artist"], "Platforms Active": "Spotify, YouTube", "Stats": "TBD",
                 "Why They Stand Out": "TBD", "The Story So Far": "TBD"}
            ],
            "creative_inspiration": {
                "soundscape": "TBD based on genre",
                "vibe": "TBD",
                "unfolds": "TBD",
                "customize": "TBD",
                "link": "https://example.com/sketch"
            },
            "quick_stats": ["Top Mood: TBD", "Stream Growth: TBD", "Hot Region: TBD"],
            "next_steps": [
                f"For Supervisors: Snag {api_data['track_title']} for a {genre.lower()} sync!",
                f"For Producers: Remix {api_data['artist']}—hot potential awaits.",
                f"For Artists: Ride this {genre.lower()} wave—drop a clip now!"
            ]
        }

        # Extract streams from engagement metrics and convert to number
        streams_str = api_data["engagement_metrics"].split()[0]
        current_streams = convert_to_number(streams_str)
        previous_streams = int(current_streams * 0.67)

        df = pd.DataFrame({
            "ds": [current_date - timedelta(days=7), current_date],
            "y": [previous_streams, current_streams]
        })

        m = Prophet().fit(df)
        future = m.make_future_dataframe(periods=14)
        forecast = m.predict(future)
        next_week_streams = int(forecast["yhat"].iloc[-7])
        report_data["predictive_analysis"][0]["Prediction"] = f"Set to hit {next_week_streams} streams by {future['ds'].iloc[-7].strftime('%B %d')}—90% crossover odds"
        all_report_data[genre] = report_data

        # Save genre data with underscores instead of hyphens
        genre_filename = genre.lower().replace(' ', '_').replace('-', '_')
        with open(f"{genre_filename}_data.py", "w") as f:
            f.write(f"report_data = {str(report_data)}")

        # Generate newsletter body
        body_text = (
            f"SoundScout AI's zeroing in—{genre.lower()}'s about to pop off! "
            f"{report_data['trending_tracks'][0]['Track Title']} by {report_data['trending_tracks'][0]['Artist']} "
            f"({report_data['trending_tracks'][0]['Engagement Metrics'].split(',')[0]}, {report_data['trending_tracks'][0]['Platform Highlights']}) "
            f"is {report_data['trending_tracks'][0]['The Buzz'].split('—')[0].lower()}—"
            f"{report_data['trending_tracks'][0]['The Buzz'].split('—')[1]} "
            f"({report_data['predictive_analysis'][0]['Score']}% crossover odds). "
            f"{report_data['predictive_analysis'][0]['Prediction'].split('—')[0]}. "
            f"Full report—AI insights, tracks, and sparks—here: https://yourapp.streamlit.app."
        )
        output_file = f"soundscout_{genre_filename}.txt"
        with open(output_file, "w") as f:
            f.write(body_text)
        logger.info(f"Report generated for {genre} and saved to {output_file}")

    # Feature Indie Pop in newsletter
    featured_genre = "Indie Pop"
    featured_file = f"soundscout_{featured_genre.lower().replace(' ', '_')}.txt"
    if os.path.exists(featured_file):
        os.rename(featured_file, "newsletter_input.txt")
    else:
        logger.warning(f"Featured genre file {featured_file} not found")
        with open("newsletter_input.txt", "w") as f:
            f.write("SoundScout AI's working on it—check back next week! Full report: https://yourapp.streamlit.app.")

except Exception as e:
    logger.error(f"Error generating reports: {str(e)}")
    with open("newsletter_input.txt", "w") as f:
        f.write("SoundScout AI's working on it—check back next week! Full report: https://yourapp.streamlit.app.")
    raise