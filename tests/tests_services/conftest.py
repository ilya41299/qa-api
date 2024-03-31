import pytest
from api_clients.services_api_clients.api_client_dog import DogApiClient
from api_clients.services_api_clients.api_client_openbrewerydb import (
    OpenbrewerydbApiClient,
)
from api_clients.services_api_clients.api_client_jsonplaceholder import (
    JsonplaceholderApiClient,
)


@pytest.fixture(scope="session")
def dog_api_client():
    return DogApiClient()


@pytest.fixture(scope="session")
def openbrewerydb_api_client():
    return OpenbrewerydbApiClient()


@pytest.fixture(scope="session")
def jsonplaceholder_api_client():
    return JsonplaceholderApiClient()
