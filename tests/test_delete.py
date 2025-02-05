import requests
import pytest
import allure
from utils.config import BASE_URL
from utils.logger import log_request


@allure.feature("Posts API")
@allure.story("Delete /posts/{post_id}")
def test_delete():
    """Test usuwania pojedynczego posta"""
    url = f"{BASE_URL}/posts/1"
    response = requests.delete(url)

    log_request(response)

    assert response.status_code == 200
    assert response.json() == {}