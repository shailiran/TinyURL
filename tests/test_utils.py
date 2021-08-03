from app.utils import base62_encoder

def test_encoder():
    response = base62_encoder(10)
    assert response == '00000A'

    response = base62_encoder(15)
    assert response == '00000F'

    response = base62_encoder(52)
    assert response == '00000q'

    response = base62_encoder(89)
    assert response == '00001R'

    response = base62_encoder(200)
    assert response == '00003E'
