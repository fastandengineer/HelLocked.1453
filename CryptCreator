#!/usr/bin/ env python
# -*- coding: utf-8 -*-

import hashlib
from getpass import getpass
from hashlib import sha1
import hashlib as hasher

print("\033[91m"+"""
+--------------------------CryptCreator--------------------------+
|								 |
|                     Welcome to CryptCreator			 |
|			       v1.0				 |
|			 					 |
| Create The Your MD5 - SHA1 - SHA224 - SHA256 - SHA384 - SHA512 |
+----------------------------------------------------------------+
C0D3R T34M = HelLocked.1453							   


"""+"\033[0m")

#MD5
key = raw_input( "Enter the anything : " )
print("Your MD5 = " + hashlib.md5( key ).hexdigest())

#SHA1
sha1 = sha1(key.encode('utf-8'))
print("Your SHA1 = " + sha1.hexdigest())

#SHA224
sifreleyici = hasher.sha224()
sifreleyici.update(key.encode("utf-8"))
hash = sifreleyici.hexdigest()
print("Your SHA224 = " + hash)

#SHA256
sifreleyici = hasher.sha256()
sifreleyici.update(key.encode("utf-8"))
hash = sifreleyici.hexdigest()
print("Your SHA256 = " + hash)

#SHA384
sifreleyici = hasher.sha384()
sifreleyici.update(key.encode("utf-8"))
hash = sifreleyici.hexdigest()
print("Your SHA384 = " + hash)

#SHA512
sifreleyici = hasher.sha512()
sifreleyici.update(key.encode("utf-8"))
hash = sifreleyici.hexdigest()
print("Your SHA512 = " + hash)
