import requests


def test_response_code(request_url, correct_status_code):
    response = requests.get(url=request_url)
    assert response.status_code == correct_status_code, response.json()
