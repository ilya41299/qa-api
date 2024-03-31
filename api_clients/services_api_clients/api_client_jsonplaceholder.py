from yarl import URL
from api_clients.api_client import HTTPClient
from enums.request_methods import RequestMethods
import requests


class JsonplaceholderApiClient(HTTPClient):
    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url

    def get_post(self, id: int) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            url=URL(self.base_url).with_path(f"posts/{id}"),
        )

    def get_filtered_post(self, query: dict = None) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            url=URL(self.base_url).with_path("posts").with_query(query),
        )

    def create_post(self, payload: dict):
        return self.make_request(
            method=RequestMethods.POST,
            url=URL(self.base_url).with_path("posts"),
            payload=payload,
        )

    def patch_post(self, payload: dict, post_id: int) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.PATCH,
            url=URL(self.base_url).with_path(f"posts/{post_id}"),
            payload=payload,
        )

    def delete_post(self, id: int) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.DELETE,
            url=URL(self.base_url).with_path(f"posts/{id}"),
        )

    def get_post_data(self, path: str) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            url=URL(self.base_url).with_path(path),
        )
