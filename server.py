from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory vote count (replace with a database in production)
vote_counts = {"thumbs_up": 0, "confused": 0}

class VoteUpdate(BaseModel):
    thumbs_up: int
    confused: int

@app.get("/")
def home():
    return {"message": "FastAPI is running!"}

@app.get("/vote_counts")
def get_votes():
    return vote_counts

@app.post("/update_votes")
def update_votes(vote: VoteUpdate):
    vote_counts["thumbs_up"] = vote.thumbs_up
    vote_counts["confused"] = vote.confused
    return {"message": "Votes updated successfully"}
