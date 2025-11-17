from src.api import get_status

def test_api_status():
    assert get_status() == "OK"
