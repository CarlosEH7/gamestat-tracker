from flask import Blueprint, render_template
import requests
import os

# Load environment variables
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

# Define the blueprint
leagues_bp = Blueprint('leagues', __name__)

@leagues_bp.route('/leagues')
def leagues():
    url = "https://api-nba-v1.p.rapidapi.com/leagues"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        leagues_data = response.json().get("response", [])
    except requests.RequestException as e:
        print(f"Error fetching leagues: {e}")
        leagues_data = []

    return render_template("leagues.html", leagues=leagues_data)

@leagues_bp.route('/leagues/<string:league_key>/teams')
def teams_by_league(league_key):
    url = "https://api-nba-v1.p.rapidapi.com/teams"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        teams = response.json().get("response", [])

        filtered_teams = []
        for team in teams:
            if league_key in team.get("leagues", {}):
                filtered_teams.append(team)

    except requests.RequestException as e:
        print(f"Error fetching teams by league: {e}")
        filtered_teams = []

    return render_template("teams.html", teams=filtered_teams, league_key=league_key)
