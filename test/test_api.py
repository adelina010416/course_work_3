from app import app


right_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_api_posts():
    response = app.test_client().get("/api/posts")
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == list
    assert set(api_response[0].keys()) == right_keys


def test_api_post():
    response = app.test_client().get("/api/posts/1")
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == dict
    assert set(api_response.keys()) == right_keys
