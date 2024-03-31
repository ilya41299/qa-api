from abc import ABC
from collections.abc import Mapping, Sequence
from typing import TypeAlias
from yarl import URL
from enums.request_methods import RequestMethods
import requests


PrimitiveData: TypeAlias = str | int | float | bool | None
JsonType: TypeAlias = Mapping[str, "JsonType"] | Sequence["JsonType"] | PrimitiveData


class HTTPClient(ABC):
    verify: bool = False

    def make_request(
        self,
        method: RequestMethods,
        url: URL,
        headers: "JsonType" = None,
        payload: "JsonType" = None,
        json: "JsonType" = None,
        files: list = None,
    ) -> requests.models.Response:
        """Выполнение http-запроса"""
        return requests.request(
            method,
            url=str(url),
            headers=headers,
            data=payload,
            json=json,
            files=files,
            verify=self.verify,
        )
