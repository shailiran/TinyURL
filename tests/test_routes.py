from app.models import URL

def test_base_route_status(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_post_method_not_found(client):
    response = client.post('/', data={'nm': 'original'})
    assert response.status_code == 302

def test_post_method_found(client):
    response = client.post('/', data={'nm': 'original'})
    response = client.post('/', data={'nm': 'original'})
    assert response.status_code == 302

def test_post_method_not_found(client):
    response = client.post('/', data={'nm': 'original'})
    assert response.status_code == 302

def test_display_route(client):
    response = client.get('/display/000001')
    assert response.status_code == 200

def test_display_route(client):
    post_response = client.post('/', data={'nm': 'original'})
    assert post_response.status_code == 302

    url = URL.query.filter_by(original_url='original').first()
    display_url = '/display/' + url.short_url
    response = client.get(display_url)
    assert response.status_code == 200

def test_short_url_exist_route(client):
    post_response = client.post('/', data={'nm': 'original'})
    assert post_response.status_code == 302

    url = URL.query.filter_by(original_url='original').first()
    get_response = client.get(url.short_url)
    assert get_response.status_code == 302

def test_short_url_not_exist_route(client):
    response = client.get('/12')
    assert 'URL does not exist' in response.data
