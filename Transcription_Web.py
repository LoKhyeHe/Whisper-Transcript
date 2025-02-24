import streamlit as st
import json
import os

VOTE_FILE = "votes.json"

# Load vote counts from a file
def load_votes():
    if os.path.exists(VOTE_FILE):
        with open(VOTE_FILE, "r") as f:
            return json.load(f)
    return {"thumbs_up": 0, "confused": 0}

# Save vote counts to a file
def save_votes(votes):
    with open(VOTE_FILE, "w") as f:
        json.dump(votes, f)

# API Endpoint (Simulated)
st.set_page_config(page_title="Live Vote Count", page_icon="📊")

st.title("Live Vote Count Dashboard")

# Read votes
votes = load_votes()

# Display votes
st.metric("👍 Thumbs Up", votes["thumbs_up"])
st.metric("😕 Confused", votes["confused"])

# Handle incoming updates
st.write("To update votes, send a `POST` request to this app.")

# Store API key securely (optional)
API_KEY = "Boobs"

# Expose a basic API for updating votes
import streamlit.web.server.websocket_headers as st_ws
import streamlit.web.server.routes as st_routes

@st_routes.add_route("/update_votes", methods=["POST"])
def update_votes():
    import flask
    request = flask.request
    if request.headers.get("API-KEY") != API_KEY:
        return {"error": "Unauthorized"}, 403

    try:
        data = request.json
        votes["thumbs_up"] = data["thumbs_up"]
        votes["confused"] = data["confused"]
        save_votes(votes)
        return {"message": "Votes updated successfully"}
    except Exception as e:
        return {"error": str(e)}, 400
