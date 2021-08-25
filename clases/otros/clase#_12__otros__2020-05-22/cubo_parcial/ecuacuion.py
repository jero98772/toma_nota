print("introdusca las dimenciones del cubo")
#se asume que el usuario solo ingresara numeros naturales mayores a 0
x = int(input("x"))
y = int(input("y"))
z = int(input("z"))
print("introdusca un punto")
xp = int(input("x"))
yp = int(input("y"))
zp = int(input("z"))
dot = [xp,yp,zp]
cube = [x,y,z]
def isIn(dot,cube):
	#asumiendo que el cubo esta ubicado en 0,0,0
	if -1*(cube[0]/2)<dot[0]<cube[0]/2 and -1*(cube[1]/2)<dot[1]<cube[1]/2 and -1*(cube[2]/2)<dot[2]<cube[2]/2:print("el punto esta adentro del cubo")
	else:print("el punto no esta adentro del cubo")
isIn(dot,cube)