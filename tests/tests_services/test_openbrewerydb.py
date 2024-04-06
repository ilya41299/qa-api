import pytest
from utils.data_readers.csv_reader import csv_brewery_types_reader


@pytest.mark.parametrize("brewery_type", csv_brewery_types_reader())
def test_get_brewery_by_type(openbrewerydb_api_client, brewery_type):
    response = openbrewerydb_api_client.get_brewery_by_type(brewery_type=brewery_type)
    response_json = response.json()
    assert response.status_code == 200, response_json
    assert all([brewery["brewery_type"] == brewery_type for brewery in response_json])


def test_get_brewery_default_per_page(openbrewerydb_api_client):
    response = openbrewerydb_api_client.get_all_breweries()
    response_json = response.json()
    assert response.status_code == 200, response_json
    assert len(response_json) == 50


@pytest.mark.parametrize(
    ("per_page", "length"),
    [
        (199, 199),
        (200, 200),
        (201, 200),
    ],
)
def test_get_brewery_per_page(openbrewerydb_api_client, per_page, length):
    response = openbrewerydb_api_client.get_all_breweries(query={"per_page": per_page})
    response_json = response.json()
    assert response.status_code == 200, response_json
    assert len(response_json) == length


@pytest.mark.parametrize(
    "country",
    [
        "south_korea",
        "United States",
    ],
)
def test_get_brewery_by_country(openbrewerydb_api_client, country):
    response = openbrewerydb_api_client.get_metadata(query={"by_country": country})
    assert response.status_code == 200, response.json()
    assert response.json()


@pytest.mark.parametrize(
    "postal_code",
    [
        "92101",
        "94123",
    ],
)
def test_filter_brewery_by_postal_code(openbrewerydb_api_client, postal_code):
    response = openbrewerydb_api_client.get_all_breweries(
        query={"by_postal": postal_code}
    )
    response_json = response.json()
    assert response.status_code == 200, response_json
    assert all(postal_code in brewery["postal_code"] for brewery in response_json)
