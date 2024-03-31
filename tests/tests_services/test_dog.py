import pytest
from schemes.dog_schemes import RandomImageScheme, AllBreedsScheme


def test_get_random_dog_image(dog_api_client):
    response = dog_api_client.get_random_dog_image()
    response_json = response.json()
    random_image = RandomImageScheme.model_validate(response_json)

    assert response.status_code == 200, response_json
    assert random_image.status == "success"


def test_get_get_all_breeds(dog_api_client):
    response = dog_api_client.get_all_breeds()
    response_json = response.json()
    all_breeds = AllBreedsScheme.model_validate(response_json)

    assert response.status_code == 200, response_json
    assert all_breeds.status == "success"
    assert len(all_breeds.message) > 0


@pytest.mark.parametrize(
    ["breed", "code"],
    [
        ("afghan", 200),
        ("no-exist-breed", 404),
    ],
)
def test_get_get_all_subbreed_images(dog_api_client, breed, code):
    response = dog_api_client.get_all_subbreed_images(breed=breed)
    response_json = response.json()
    assert response.status_code == code, response_json
    assert response_json


@pytest.mark.parametrize(
    ["breed", "code"],
    [
        ("borzoi", 200),
        ("boxer", 200),
        ("no-exist-breed", 404),
    ],
)
def test_get_dog_by_breed(dog_api_client, breed, code):
    assert dog_api_client.get_random_dog_image_by_breed(breed=breed).status_code == code


@pytest.mark.parametrize(
    ["breed", "code"],
    [
        ("hound", 200),
        ("akita", 200),
        ("no-exist-breed", 404),
    ],
)
def test_get_subbreed_by_breed(dog_api_client, breed, code):
    assert dog_api_client.get_subbreeds_by_breed(breed=breed).status_code == code
