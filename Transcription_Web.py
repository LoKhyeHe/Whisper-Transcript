import streamlit as st
import firebase_admin
from firebase_admin import credentials, db

# Firebase Setup
cred = credentials.Certificate("nesherbot-firebase-adminsdk-fbsvc-15b8ace860.json")  # Your Firebase JSON file
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://nesherbot-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

votes_ref = db.reference("votes")

st.title("📊 Live Voting Results")

# Fetch Live Votes
votes = votes_ref.get() or {"thumbs_up": 0, "confused": 0}

# Display Votes
st.metric(label="👍 Thumbs Up", value=votes["thumbs_up"])
st.metric(label="😕 Confused", value=votes["confused"])

# Refresh Button
if st.button("🔄 Refresh"):
    votes = votes_ref.get()
    st.experimental_rerun()
