from app.services.stats_api import get_latest_games

def test_get_latest_games():
    data = get_latest_games()
    assert "data" in data
