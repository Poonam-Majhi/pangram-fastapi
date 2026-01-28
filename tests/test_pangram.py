import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.utils import is_pangram

client = TestClient(app)

#Unit tests for logic

@pytest.mark.parametrize("text, expected", [
    ("The quick brown fox jumps over the lazy dog", True),
    ("Sphinx of black quartz, judge my vow", True),
    ("Pack my box with five dozen liquor jugs.", True),
    ("Hello World", False),
    ("", False),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", True),
    ("abcdefghijklmnopqrstuvwxy", False),
])
def test_is_pangram_logic(text, expected):
    ok, missing = is_pangram(text)
    assert ok == expected
    if expected:
        assert missing == []
    else:
        assert isinstance(missing, list)

#API tests

def test_get_pangram_true():
    r = client.get("/ispangram", params={"text": "The quick brown fox jumps over the lazy dog"})
    assert r.status_code == 200
    data = r.json()
    assert data["isPangram"] is True
    assert data["missing"] == []

def test_get_pangram_false():
    r = client.get("/ispangram", params={"text": "Hello World"})
    assert r.status_code == 200
    data = r.json()
    assert data["isPangram"] is False
    assert isinstance(data["missing"], list)
    assert 'a' in data["missing"]

def test_post_pangram():
    r = client.post("/ispangram", json={"text": "Sphinx of black quartz, judge my vow"})
    assert r.status_code == 200
    data = r.json()
    assert data["isPangran"] is True
    assert data["missing"] == []

def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"