# iss_tracker_auto.py

import requests
from datetime import datetime, UTC
import streamlit as st
import plotly.express as px
import time

# Streamlit page config
st.set_page_config(layout="centered")
st.title("🛰️ Real-Time ISS Tracker (Auto-Refresh Every 10 Seconds)")

# Placeholder to update live content
placeholder = st.empty()

while True:
    with placeholder.container():
        # Fetch ISS current location data
        url = 'http://api.open-notify.org/iss-now.json'
        response = requests.get(url).json()

        latitude = float(response['iss_position']['latitude'])
        longitude = float(response['iss_position']['longitude'])
        timestamp = response['timestamp']
        time_str = datetime.fromtimestamp(timestamp, UTC).strftime('%Y-%m-%d %H:%M:%S UTC')

        st.subheader("📍 ISS Current Coordinates")
        st.markdown(f"**Timestamp (UTC):** `{time_str}`")
        st.markdown(f"**Latitude:** `{latitude}` &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; **Longitude:** `{longitude}`")

        # Plot on Plotly world map
        fig = px.scatter_geo(
            lat=[latitude],
            lon=[longitude],
            text=[f"🌌 ISS<br>{time_str}"],
            projection="natural earth",
            title="🌍 ISS Current Position (Live)",
        )
        fig.update_traces(marker=dict(size=12, color='crimson'))
        st.plotly_chart(fig, use_container_width=True)

    time.sleep(10)  # Wait 10 seconds before updating
    placeholder.empty()  # Clear for next cycle