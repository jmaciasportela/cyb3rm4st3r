#!/usr/bin/python3
# # -*- coding: utf-8 -*-

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Generate context
backend = default_backend()
# Generate pseudo random key
key = bytes(str('12345678901234567890123456789012'), 'ascii')
# Init vecto
iv = os.urandom(16)
#Setup Cipher
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
# Init encryptor
encryptor = cipher.encryptor()
# Feed encryptor with data and finalize to obtain cryptogram
cryptogram = encryptor.update(b"a secret message") + encryptor.finalize()
# Output
print(cryptogram)

# Init decryptor
decryptor = cipher.decryptor()
clearText = decryptor.update(cryptogram) + decryptor.finalize()
print(clearText)
