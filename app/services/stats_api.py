import requests

def get_latest_games():
    url = "https://www.balldontlie.io/api/v1/games"
    response = requests.get(url)
    return response.json()
