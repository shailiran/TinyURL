def test_base_route_status(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_add_url(client, mock_url):
    response = client.post('/', data=mock_url.short_url)
    assert(302, response.status_code)
    assert(mock_url.original_url, response.location)
