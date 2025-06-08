#!/usr/bin/env python3

import sys
import base64
from Crypto.Cipher import DES3
from Crypto.Hash import SHA

# hardcoded XOR key (bytes)
KEY = bytearray.fromhex("12150F10111C1A060A1F1B1817160519")

def sitelist_xor(xs):
    result = bytearray()
    for i, c in enumerate(xs):
        result.append(c ^ KEY[i % 16])
    return result

def des3_ecb_decrypt(data):
    # hardcoded 3DES key
    key = SHA.new(b'<!@#$%^>').digest() + bytearray(4)
    des3 = DES3.new(key, DES3.MODE_ECB)
    data += bytearray(64 - (len(data) % 64))  # pad to 64
    decrypted = des3.decrypt(data)
    return decrypted.split(b'\x00')[0] or b"<empty>"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage:   {sys.argv[0]} <base64 passwd>")
        print(f"Example: {sys.argv[0]} 'jWbTyS7BL1Hj7PkO5Di/QhhYmcGj5cOoZ2OkDTrFXsR/abAFPM9B3Q=='")
        sys.exit(0)

    encrypted_password = base64.b64decode(sys.argv[1])
    passwdXOR = sitelist_xor(encrypted_password)
    password = des3_ecb_decrypt(passwdXOR).decode("utf-8", errors="ignore")
    print(f"Crypted password   : {sys.argv[1]}")
    print(f"Decrypted password : {password}")
