import pytest


@pytest.mark.parametrize("route", ["/<short_url>", "/display/<url>", "/"])
def test_route_status(client, route):
    rv = client.get(route)
    assert rv.status_code == 200