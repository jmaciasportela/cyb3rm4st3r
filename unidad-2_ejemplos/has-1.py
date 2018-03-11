#!/usr/bin/python3
# # -*- coding: utf-8 -*-

import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Generate context
backend = default_backend()
# Init digest
digest = hashes.Hash(hashes.SHA256(), backend=backend)
# Update digest
digest.update(b"a secret message")
# Obtain digest result
hash = digest.finalize()
# Output
print ("SHA256 hash: ", hash)

