#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyaes
import os

# Any mode of operation can be used; for this example CBC
key = "This_key_for_demo_purposes_only!"
iv = "InitializationVe"

ciphertext = ''

# We can encrypt one line at a time, regardles of length
encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(key, iv))
for line in file('/etc/passwd'):
    ciphertext += encrypter.feed(line)

# Make a final call to flush any remaining bytes and add paddin
ciphertext += encrypter.feed()

print repr(ciphertext)

# We can decrypt the cipher text in chunks (here we split it in half)
decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(key, iv))
decrypted = decrypter.feed(ciphertext[:len(ciphertext) / 2])
decrypted += decrypter.feed(ciphertext[len(ciphertext) / 2:])

# Again, make a final call to flush any remaining bytes and strip padding
decrypted += decrypter.feed()

print file('/etc/passwd').read() == decrypted
