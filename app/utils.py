from math import floor 

def base62_encoder(id):
    # characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    base = len(characters)
    r = id % base
    res = characters[r]
    q = floor(id / base)
    while q:
        r = q % base
        q = floor(q / base)
        res = characters[int(r)] + res
    return res.rjust(6, '0')
