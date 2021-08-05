import pytest
import logging
import sys

def test_base_route_status(client):
    rv = client.get('/')
    assert rv.status_code == 200

@pytest.mark.parametrize('original_url', ('original_1', 'original_2'))
def test_post_method(client, original_url):
    response = client.post('/', data={'nm': original_url})
    logger = logging.getLogger()
    logger.error(response.location)
    assert response.status_code == 302

@pytest.mark.parametrize('path', ('/display/000001', '/display/000002'))
def test_display_route(client, path):
    response = client.get(path)
    assert response.status_code == 200

@pytest.mark.parametrize('path', ('/000001', '/000002'))
def test_short_url_exist_route(client, path):
    response = client.get(path)
    location = 'http://localhost/original_' + path[-1]
    assert response.status_code == 302
    assert response.location == location

@pytest.mark.parametrize('path', ('/12', '/00002'))
def test_short_url_not_exist_route(client, path):
    response = client.get(path)
    assert 'URL does not exist' in response.data


    # logger = logging.getLogger()
    # logger.error(response.data)
    # logger.error(response.location)