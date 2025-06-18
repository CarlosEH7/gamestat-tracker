import os
import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

def fetch_nba_teams():
    url = "https://api-nba-v1.p.rapidapi.com/teams"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    data = res.json().get("response", [])

    nba_teams = []
    for t in data:
        name = (t.get("fullName") or t.get("name") or "").lower()
        is_nba = t.get("nbaFranchise") is True
        leagues = t.get("leagues", {})
        in_standard_league = "standard" in leagues

        if is_nba and in_standard_league and "stephen" not in name:
            standard_league = leagues.get("standard", {})
            nba_teams.append({
                "name": t.get("fullName") or t.get("name"),
                "abbreviation": t.get("abbreviation"),
                "logo_url": t.get("logo"),
                "wins": standard_league.get("win", 0),
                "losses": standard_league.get("loss", 0),
                "games_played": standard_league.get("games", 0)
            })

    return nba_teams
