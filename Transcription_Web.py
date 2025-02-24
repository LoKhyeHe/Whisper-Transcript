import streamlit as st
import requests

API_URL = "https://your-secure-api.com/vote_counts"

st.title("Live Vote Count")

# Fetch vote counts from the API
def get_vote_counts():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            return {"thumbs_up": 0, "confused": 0}
    except:
        return {"thumbs_up": 0, "confused": 0}

vote_data = get_vote_counts()

st.metric("👍 Thumbs Up", vote_data["thumbs_up"])
st.metric("😕 Confused", vote_data["confused"])
