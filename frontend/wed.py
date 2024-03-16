from itertools import *
import hashlib
import string

res = "836473307fa2a6dd0897f932dd53984e"
for w in product(f'{string.digits}{string.ascii_lowercase}', repeat=4):
    code = ''.join(w)
    text = f"MySecretNuberIs_{code}"
    text_bytes = text.encode('utf-8')
    hash_object = hashlib.md5(text_bytes)
    md5_hash = hash_object.hexdigest()
    if md5_hash == res:
        print(code)