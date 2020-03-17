import pytest
from .app import app, db


# @pytest.fixture(scope='module')
@pytest.fixture()
def context():
    db.create_all()
    yield
    db.drop_all()


def test_index(context):
    response = app.test_client().get('/events')
    assert response.status_code == 200
    assert response.json == []


@pytest.fixture
def post_event():
    response = app.test_client().post('/events', json={
        "title": "Event 1",
        "descr": "Event 1 descr",
        "dt": "2020-10-01 18:00",
        "address": "Street, 1"
    })
    return response


def test_post(context, post_event):
    response = post_event
    assert response.status_code == 201
    assert response.json['title'] == "Event 1"
    assert len(response.json['ext_id']) == 36


def test_post_validation(context):
    response = app.test_client().post('/events', json={
        "title": "Event 1",
        "descr": "Event 1 descr",
        "dt": "XXXXXXXXX",
        "address": "Street 1"
    })
    assert response.status_code == 400
    assert response.json == "{'dt': ['Not a valid datetime.']}"


def test_get(context, post_event):
    ext_id = post_event.json['ext_id']
    response = app.test_client().get(f"/events/{ext_id}")
    assert response.status_code == 200
    assert response.json['title'] == "Event 1"


def test_get_not_found(context):
    response = app.test_client().get('/events/xxxxx')
    assert response.status_code == 404


def test_delete(context, post_event):
    priv_id = post_event.json['priv_id']
    response = app.test_client().delete(f"/events/{priv_id}")
    assert response.status_code == 204
    response = app.test_client().get(f"/events/{priv_id}")
    assert response.status_code == 404


def test_update(context, post_event):
    priv_id = post_event.json['priv_id']
    ext_id = post_event.json['ext_id']
    response = app.test_client().put(f'/events/{priv_id}', json={
        "title": "Event 2",
        "descr": "Event 1 descr",
        "dt": "2020-10-01 18:00",
        "address": "Street 1"
    })
    assert response.status_code == 200
    response = app.test_client().get(f"/events/{ext_id}")
    assert response.status_code == 200
    assert response.json['title'] == 'Event 2'


