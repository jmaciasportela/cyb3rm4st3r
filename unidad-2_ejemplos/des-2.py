#!/usr/bin/python3
# # -*- coding: utf-8 -*-

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Generate context
backend = default_backend()
# Generate pseudo random key
key = bytes(str('123456789012345678901234'), 'ascii')
#Setup Cipher
cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=backend)
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
