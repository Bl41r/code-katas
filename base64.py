import base64


def to_base_64(string):
    return base64.b64encode(string).replace(b'=', b'')


def from_base_64(string):
    if len(string) % 4:
        string += b'=' * (4 - len(string) % 4)
    return base64.decodestring(string)
