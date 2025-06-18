from flask import Blueprint, render_template
from app.api_client import fetch_nba_teams  # import your API fetch function

chart_bp = Blueprint('chart', __name__)

@chart_bp.route("/chart")
def chart():
    # Fetch teams dynamically from RapidAPI
    teams = fetch_nba_teams()

    # Add logo URLs if not included by the API (or adjust accordingly)
    for team in teams:
        if 'logo_url' not in team or not team['logo_url']:
            team['logo_url'] = f"https://a.espncdn.com/i/teamlogos/nba/500/{team['abbreviation']}.png"

    return render_template("team_list.html", teams=teams)
