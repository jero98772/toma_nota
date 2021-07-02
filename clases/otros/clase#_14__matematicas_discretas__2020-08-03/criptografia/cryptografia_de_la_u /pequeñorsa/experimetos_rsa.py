e = 5
d = 17
n = 21
dvalue = 3
enc = (dvalue**e)%n
dec = (enc**e)%n
print(dvalue,enc,dec)
#3 12 3
dec = (dvalue**e)%n
enc = (dec**e)%n
print(dvalue,enc,dec)
#3 3 12
d = 245
n = 309
dvalue = 3
enc = (dvalue**e)%n
dec = (enc**e)%n
print(dvalue,enc,dec)
#3 12 3
dec = (dvalue**e)%n
enc = (dec**e)%n
print(dvalue,enc,dec)

