from api_clients.api_client import HTTPClient
from enums.request_methods import RequestMethods
import requests


class DogApiClient(HTTPClient):
    def __init__(self, base_url="https://dog.ceo"):
        super().__init__(base_url=base_url)

    def get_random_dog_image(self) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            path="api/breeds/image/random",
        )

    def get_all_breeds(self) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            path="api/breeds/list/all",
        )

    def get_random_dog_image_by_breed(self, breed: str) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            path=f"api/breed/{breed}/images/random",
        )

    def get_subbreeds_by_breed(self, breed: str) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            path=f"api/breed/{breed}/list",
        )

    def get_all_subbreed_images(self, breed: str) -> requests.models.Response:
        return self.make_request(
            method=RequestMethods.GET,
            path=f"api/breed/hound/{breed}/images",
        )
