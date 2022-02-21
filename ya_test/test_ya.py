import pytest
import requests


def test_check_ya(base_url, status_code):
    response = requests.get(base_url)
    assert response.status_code == status_code


@pytest.mark.parametrize("id", ["qwewtegfufngig", 23, 0, -1])
def test_negative_yandex(base_url, id, error_status_code):
    response = requests.get(f"{base_url}/{id}")
    assert response.status_code == error_status_code
