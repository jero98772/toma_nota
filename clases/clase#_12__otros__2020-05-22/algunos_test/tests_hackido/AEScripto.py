from Crypto.Cipher import AES
from Crypto import Random
from hashlib import sha256
import base64
import hashlib
def enPassowrd(password):
	hashPassowrd = sha256(password.encode("utf-8")).digest()
	return hashPassowrd
def encriptar(mensaje,key):
	print(key,"logitud",len(key))
	iv = Random.new().read(AES.block_size)
	cif = AES.new(key, AES.MODE_CFB,iv)
	mensaje = iv + cif.encrypt(mensaje)
	return base64.b64encode(mensaje)
def desencriptar(mensaje,key):
	#unpad = lambda s : s[:-ord(s[len(s)-1:])]	
	iv = Random.new().read(AES.block_size)
	enc = base64.b64decode(enc)
	iv = enc[:16]
	dec = AES.new(key, AES.MODE_CFB,iv)
	mensaje = iv + dec.decrypt(mensaje)	
	return mensaje

# AES 256 encryption/decryption using pycrypto library
#https://www.quickprogrammingtips.com/python/aes-256-encryption-and-decryption-in-python.html este funciona

 
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 
password = "d0095d2938111626"
 
 
def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))
 
 
# First let us encrypt secret message
#encrypted = encrypt("This is a secret message y me perdi mas mas mas mas ", password)
#print(encrypted)
 
# Let us decrypt using our original password
#decrypted = decrypt(encrypted, password)
#print(bytes.decode(decrypted))
key = "d0095d2938111626"
msg = "mundo bello hola "
#nuevo sin complicarme 
def encryptE(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
def decryptE(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    mensaje =  unpad(cipher.decrypt(enc[16:]))
    return mensaje
enc = encryptE(msg, key)
print(str(decryptE(enc, key).decode()))
"""
un = pad(msg)
print(un)
algo = unpad(un)
print(algo)
print(len(msg))
print(len(un))#diferente tamaño 32 vs 17 
print(len(algo))
"""