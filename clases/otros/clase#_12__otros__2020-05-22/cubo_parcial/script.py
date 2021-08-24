a = 1
b = 1
c = 202
x = 1 
y = 1
z = -4
z2 = -4
d=(a*x+b*y+c*z)
print(d)
hipo = ((a**2+b**2+c**2)**(1/2))
print(hipo)
distancia = a*x+b*y+c*z+d/hipo
print(distancia)
d2=(a*x+b*y+c*z2)
print(d2)
hipo2 = ((a**2+b**2+c**2)**(1/2))
print(hipo2)
distancia2 = a*x+b*y+c*z2+d/hipo2
print(distancia2)

"""
d=(c*z)
#print(d)
hipo = ((c**2)**(1/2))
#print(hipo)
distancia = (c*z+d)/hipo
print(distancia)
d2=(c*z2)
hipo = ((c**2)**(1/2))
distancia2 = (c*z2+d2)/hipo
print(distancia2)
"""
print(str(z)+"<"+str(c)+"<"+str(z2)+str(bool(z<c<z2)))
#print(str(d)+"<"+str(c)+"<"+str(d2)+str(bool(d<c<d2)))
print(str(distancia)+"<"+str(c)+"<"+str(distancia2)+str(bool(distancia<c<distancia2)))
print(str(c)+">"+str(distancia)+str(bool(distancia<0)))
print(str(c)+">"+str(distancia2)+str(bool(distancia2<0)))
