from abc import ABC
from collections.abc import Mapping, Sequence
from typing import TypeAlias
from yarl import URL
from enums.request_methods import RequestMethods
import requests

PrimitiveData: TypeAlias = str | int | float | bool | None
JsonType: TypeAlias = Mapping[str, "JsonType"] | Sequence["JsonType"] | PrimitiveData


class HTTPClient(ABC):
    base_url: str

    def __init__(self, base_url: str):
        self.base_url = base_url

    def make_request(
        self,
        method: RequestMethods,
        path: str,
        query: dict = None,
        headers: "JsonType" = None,
        payload: "JsonType" = None,
        json: "JsonType" = None,
        files: list = None,
    ) -> requests.models.Response:
        """Выполнение http-запроса"""
        return requests.request(
            method,
            url=str(URL(self.base_url).with_path(path).with_query(query)),
            headers=headers,
            data=payload,
            json=json,
            files=files,
        )
