print("introdusca las dimenciones del cubo")
x = input("x")
y = input("y")
z = input("z")
#puntos = [[0,0,0],[0,0,z],[0,y,0],[x,0,0],[0,y,z],[x,0,z],[x,y,0],[x,y,z]]
print("introsuca un punto")
xp = input("x")
yp = input("y")
zp = input("z")
dot = [xp,yp,zp]
plain = []
def genPlano(dot,cubeAxisPlain):
	d=a*x+b*y+c*z
	hippo = ((a**2+b**2+c**2)**(1/2))
