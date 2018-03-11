#!/usr/bin/python3
# # -*- coding: utf-8 -*-

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Original message
message = b"a secret message"
print('1- ORIGINAL MESSAGE: ', message)
# Generate context
backend = default_backend()
# Generate pseudo random key
key = bytes(str('12345678901234567890123456789012'), 'ascii')
#Setup Cipher
cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
# Init encryptor
encryptor = cipher.encryptor()
# Feed encryptor with data and finalize to obtain cryptogram
cryptogram = encryptor.update(message) + encryptor.finalize()
# Output
print('2- ENCRYPTED MESSAGE WITH STATIC KEY AND ECB: ', cryptogram)

# Init decryptor
decryptor = cipher.decryptor()
clearText = decryptor.update(cryptogram) + decryptor.finalize()
print('3- DECRYPTED MESSAGE: ', clearText)
print('ORIGINAL AND DECRYPTED MESSAGES ARE EQUAL ->', message.decode('utf8') == clearText.decode('utf8'))
