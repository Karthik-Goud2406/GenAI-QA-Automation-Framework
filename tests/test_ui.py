from src.ui import render_homepage

def test_homepage_render():
    assert "<h1>" in render_homepage()
