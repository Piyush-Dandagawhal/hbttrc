import streamlit as st
import requests
from datetime import date

API_URL = "https://script.google.com/macros/s/AKfycbx_1N1YkvsSlf52a1PbEQjXyjHzSok8pSKlMTy1qIqis0hMGabzeCxmq3mHVePN3a4JFA/exec"

st.set_page_config(layout="centered")
st.title("🌱 Daily Tracker")

today = date.today().isoformat()

st.subheader(f"📅 {today}")

ukulele = st.checkbox("🎸 Practiced ukulele")
reading = st.checkbox("📖 Read 15 minutes")
gym = st.checkbox("🏋️ Went to the gym")

st.markdown("### 💧 Water")
water = st.number_input(
    "Glasses of water",
    min_value=0,
    step=1
)

if st.button("✅ Save Today", use_container_width=True):
    payload = {
        "date": today,
        "ukulele": ukulele,
        "reading": reading,
        "water": water,
        "gym": gym
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        st.success("Saved to Google Sheet!")
    else:
        st.error("Something went wrong")
