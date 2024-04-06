import pytest
from utils.data_readers.json_reader import json_posts_reader
from schemes.jsonplaceholders_schemes import (
    CommentScheme,
    PhotoScheme,
    AlbumScheme,
    TodosScheme,
    PostsScheme,
)


def test_create_post(jsonplaceholder_api_client):
    post_data = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    response = jsonplaceholder_api_client.create_post(payload=post_data)
    response_json = response.json()
    assert response.status_code == 201, response_json
    assert set(post_data).issubset(set(response_json))


def test_update_post(jsonplaceholder_api_client):
    old_post_data = {
        "title": "old_title",
        "body": "old_body",
        "userId": 1,
    }
    new_post_json = jsonplaceholder_api_client.create_post(payload=old_post_data).json()
    new_post_id = new_post_json["id"]
    new_post_data = {
        "title": "new_title",
        "body": "new_body",
    }

    response = jsonplaceholder_api_client.patch_post(
        payload=new_post_data, post_id=new_post_id
    )
    response_json = response.json()
    assert response.status_code == 200, response_json
    assert set(new_post_data).issubset(set(response_json))


def test_delete_post(jsonplaceholder_api_client):
    post_data = {
        "title": "old_title",
        "body": "old_body",
        "userId": 1,
    }
    post_json = jsonplaceholder_api_client.create_post(payload=post_data).json()
    post_id = post_json["id"]

    response = jsonplaceholder_api_client.delete_post(id=post_id)

    assert response.status_code == 200, response.json()
    response = jsonplaceholder_api_client.get_post(id=post_id)
    assert response.status_code == 404, response.json()


@pytest.mark.parametrize(
    ("route", "scheme"),
    [
        ("posts/1/comments", CommentScheme),
        ("albums/1/photos", PhotoScheme),
        ("users/1/albums", AlbumScheme),
        ("users/1/todos", TodosScheme),
        ("users/1/posts", PostsScheme),
    ],
)
def test_check_equivalent_routes(jsonplaceholder_api_client, route, scheme):
    response = jsonplaceholder_api_client.get_post_data(path=route)
    first_object = response.json()[0]
    assert response.status_code == 200, response.json()
    assert scheme.model_validate(first_object)


@pytest.mark.parametrize(("filter_key", "filter_value"), json_posts_reader())
def test_filtering_posts(jsonplaceholder_api_client, filter_key, filter_value):
    response = jsonplaceholder_api_client.get_filtered_post(
        query={filter_key: filter_value}
    )
    response_json = response.json()

    assert response.status_code == 200, response_json
    assert all(post[filter_key] == filter_value for post in response_json)
