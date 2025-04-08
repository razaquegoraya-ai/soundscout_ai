import streamlit as st
from indie_pop_data import report_data as indie_pop_data
from country_data import report_data as country_data
from hip_hop_data import report_data as hip_hop_data
from rock_data import report_data as rock_data
from folk_data import report_data as folk_data

all_data = {
    "Indie Pop": indie_pop_data,
    "Country": country_data,
    "Hip-Hop": hip_hop_data,
    "Rock": rock_data,
    "Folk": folk_data
}

st.title("SoundScout AI Report: Pick Your Genre")
genre = st.selectbox("Choose a genre:", list(all_data.keys()))
report_data = all_data[genre]

st.write(f"**Generated On:** {report_data['date']}")
st.write(f"**Scope:** Emerging Breakouts in {report_data['genre']}")

st.header("1. Trending Tracks")
st.write("*What's Lighting Up the Airwaves*")
st.table(report_data['trending_tracks'])

st.header("2. Predictive Trend Analysis")
st.write("*What's Next, According to AI*")
st.table(report_data['predictive_analysis'])

st.header("3. Artist Spotlight: Emerging Talent")
st.write("*Who's Ready to Shine*")
st.table(report_data['artist_spotlight'])

st.header("4. Creative Inspiration")
st.write("*A Spark for Your Next Project*")
for key, value in report_data['creative_inspiration'].items():
    st.write(f"**{key.capitalize()}:** {value}")

st.header("5. Quick Stats Summary")
for stat in report_data['quick_stats']:
    st.write(f"- {stat}")

st.header("6. Next Steps: Your Cheat Sheet")
for step in report_data['next_steps']:
    st.write(f"- {step}")

st.write("**Export Options:** Download as PDF | Share via Email | Save to Dashboard")
st.write("**Sign Up:** [Join our newsletter!](https://example.com/newsletter)")