import requests
import pytest
from utils.logger import log_request
from utils.config import BASE_URL


def test_get_post():
    """Test pobierania pojedynczego posta"""
    url = f"{BASE_URL}/posts/1"
    response = requests.get(url)

    log_request(response)

    assert response.status_code == 200
    assert response.json()["id"] == 1