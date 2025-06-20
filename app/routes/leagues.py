import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")  # e.g. "api-nba-v1.p.rapidapi.com"

leagues_bp = Blueprint("leagues", __name__)

@leagues_bp.route("/leagues")
def leagues():
    url = "https://api-nba-v1.p.rapidapi.com/leagues"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.RequestException as e:
        print("Error fetching leagues:", e)
        return render_template("leagues.html", leagues=[])

    leagues = data.get("response", [])

    basketball_leagues = []
    for league in leagues:
        if isinstance(league, dict):
            sport = league.get("sport")
            if isinstance(sport, str) and sport.lower() == "basketball":
                basketball_leagues.append(league)




    return render_template("leagues.html", leagues=basketball_leagues)
