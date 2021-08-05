from app.models import URL
import pytest

def test_base_route_status(client):
    rv = client.get('/')
    assert rv.status_code == 200

@pytest.mark.parametrize('original_url', ('original_1', 'original_2'))
def test_post_method_not_found(client, original_url):
    response = client.post('/', data={'nm': original_url})
    assert response.status_code == 302

@pytest.mark.parametrize('original_url', ('original_1', 'original_2'))
def test_post_method_found(client, original_url):
    response = client.post('/', data={'nm': original_url})
    response = client.post('/', data={'nm': original_url})
    assert response.status_code == 302

@pytest.mark.parametrize('original_url', ('original_3', 'original_4'))
def test_post_method_not_found(client, original_url):
    response = client.post('/', data={'nm': original_url})
    assert response.status_code == 302

@pytest.mark.parametrize('path', ('/display/000001', '/display/000002'))
def test_display_route(client, path):
    response = client.get(path)
    assert response.status_code == 200

def test_short_url_exist_route(client):
    post_response = client.post('/', data={'nm': 'original_1'})
    assert post_response.status_code == 302
    url = URL.query.filter_by(original_url='original_1').first()
    get_response = client.get(url.short_url)
    assert get_response.status_code == 302

@pytest.mark.parametrize('path', ('/12', '/00002'))
def test_short_url_not_exist_route(client, path):
    response = client.get(path)
    assert 'URL does not exist' in response.data

