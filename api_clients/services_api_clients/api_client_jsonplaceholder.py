from api_clients.api_client import HTTPClient
from enums.request_methods import RequestMethods
import requests


class JsonplaceholderApiClient(HTTPClient):
    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        super().__init__(base_url=base_url)

    def get_post(self, id: int) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            path=f"posts/{id}",
        )

    def get_filtered_post(self, query: dict = None) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            path="posts",
            query=query,
        )

    def create_post(self, payload: dict):
        return self.make_request(
            method=RequestMethods.POST,
            path="posts",
            payload=payload,
        )

    def patch_post(self, payload: dict, post_id: int) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.PATCH,
            path=f"posts/{post_id}",
            payload=payload,
        )

    def delete_post(self, id: int) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.DELETE,
            path=f"posts/{id}",
        )

    def get_post_data(self, path: str) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            path=path,
        )
