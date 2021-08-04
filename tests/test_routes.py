def test_base_route_status(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_post_method(client, mock_url):
    short_url = mock_url.short_url
    response = client.post('/', data=short_url)
    assert 302, response.status_code
    assert mock_url.original_url, response.location

def test_short_url_route(client, mock_url):
    short_url = mock_url.short_url
    response = client.get('/<short_url>')
    assert 302, response.status_code
    assert mock_url.original_url, response.location

def test_display_route(client, mock_url):
    short_url = mock_url.short_url
    response = client.get('/display/<short_url>')
    assert 302, response.status_code
    assert mock_url.original_url, response.location