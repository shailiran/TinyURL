def test_route_status(client):
    rv = client.get('/')
    assert rv.status_code == 200

# def test_empty_db(client):
#     """Start with a blank database."""

#     rv = client.get('/')
#     assert b'No entries here so far' in rv.data