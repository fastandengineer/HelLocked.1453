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

while 1:

  #MD5
  key = raw_input( "Enter the anything : " )
  print("\033[93m"+"Your MD5 = " + hashlib.md5( key ).hexdigest()+"\033[0m")

  #SHA1
  sifreleyici = hasher.sha1()
  sifreleyici.update(key.encode("utf-8"))
  hash = sifreleyici.hexdigest()
  print("\033[93m"+"Your SHA1 = " + hash+"\033[0m")

  #SHA224
  sifreleyici = hasher.sha224()
  sifreleyici.update(key.encode("utf-8"))
  hash = sifreleyici.hexdigest()
  print("\033[93m"+"Your SHA224 = " + hash+"\033[0m")

  #SHA256
  sifreleyici = hasher.sha256()
  sifreleyici.update(key.encode("utf-8"))
  hash = sifreleyici.hexdigest()
  print("\033[93m"+"Your SHA256 = " + hash+"\033[0m")

  #SHA384
  sifreleyici = hasher.sha384()
  sifreleyici.update(key.encode("utf-8"))
  hash = sifreleyici.hexdigest()
  print("\033[93m"+"Your SHA384 = " + hash+"\033[0m")

  #SHA512
  sifreleyici = hasher.sha512()
  sifreleyici.update(key.encode("utf-8"))
  hash = sifreleyici.hexdigest()
  print("\033[93m"+"Your SHA512 = " + hash+"\033[0m"+"\n\n\n")

  key = ""
