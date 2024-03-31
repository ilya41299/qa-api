import pytest

from utils.data_readers import POSTS_JSON_FILE_PATH
import json


def json_posts_reader():
    with open(POSTS_JSON_FILE_PATH) as posts_file:
        posts_data = json.load(posts_file)
        for post_data in posts_data:
            yield pytest.param(
                post_data["filter"], post_data["value"], id=post_data["filter"]
            )
