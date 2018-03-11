#!/usr/bin/python3
# # -*- coding: utf-8 -*-

import sys
import binascii
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

filename = str(sys.argv[1])

try: 
    # Open file with read and binary mode
    file = open(filename, 'rb')
except IOError:
    print('File -->' + filename + '<-- not found')
    # Exit with error
    exit(1)

# Generate context
backend = default_backend()
# Init digest
digest = hashes.Hash(hashes.MD5(), backend=backend)
# Load file content 
digest.update(file.read())
# Obtain digest result
hash = digest.finalize()
# Return the hexadecimal representation of the binary data. Every byte of data is converted 
# into the corresponding 2-digit hex representation. The resulting string is therefore twice 
# as long as the length of data.
human_ready_output = binascii.hexlify(hash)
print("INPUT: %s  <--> MD5 hash: %s " % (filename, str(human_ready_output, 'utf8')))