from app.utils import base62_encoder

def test_encoder():
    response = base62_encoder(10)
    assert response == '00000a'

    response = base62_encoder(15)
    assert response == '00000f'

    response = base62_encoder(52)
    assert response == '00000Q'

    response = base62_encoder(89)
    assert response == '00001r'

    response = base62_encoder(200)
    assert response == '00003e'
