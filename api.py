import os
from fastapi import FastAPI, Request, HTTPException, Query
import requests
from dotenv import load_dotenv

load_dotenv()

TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_TOKEN = os.getenv("TWITCH_TOKEN")
API_PASSWORD = os.getenv("API_PASSWORD")
TWITCH_API_URL = 'https://api.twitch.tv/helix/streams'

app = FastAPI()

@app.get("/stream")
async def get_stream_info(
    request: Request,
    user_login: str = Query(..., description="Twitch user login")
):
    api_key = request.headers.get("X-API-Key")
    if api_key != API_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized: invalid API key")

    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {TWITCH_TOKEN}"
    }

    params = {
        "user_login": user_login
    }

    try:
        response = requests.get(TWITCH_API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if not data["data"]:
            raise HTTPException(status_code=404, detail="❌ Stream not found or offline")

        stream = data["data"][0]

        return {
            "user_name": stream["user_name"],
            "title": stream["title"],
            "game_name": stream["game_name"],
            "viewer_count": stream["viewer_count"],
            "started_at": stream["started_at"],
            "language": stream["language"],
            "type": stream["type"]
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Twitch API request error: {str(e)}")
