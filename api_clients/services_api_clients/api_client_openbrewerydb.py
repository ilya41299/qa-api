from api_clients.api_client import HTTPClient
from enums.request_methods import RequestMethods
import requests


class OpenbrewerydbApiClient(HTTPClient):
    def __init__(self, base_url="https://api.openbrewerydb.org"):
        super().__init__(base_url=base_url)

    def get_all_breweries(self, query: dict = None) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            path="v1/breweries",
            query=query,
        )

    def get_metadata(self, query: dict) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            path="v1/breweries/meta",
            query=query,
        )

    def get_brewery_by_type(self, brewery_type: str) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            path="v1/breweries",
            query={"by_type": brewery_type},
        )
