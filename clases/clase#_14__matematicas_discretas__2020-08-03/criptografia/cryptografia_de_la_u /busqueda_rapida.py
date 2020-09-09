import hashlib
import random

password = str(random.randrange(10000))
print(str(hashlib.sha256(password.encode('utf-8')).hexdigest()))

f = open("secreto.txt","w")
f.write(password)
f.close()
