#cuantos bloques se debe mover el gomba, "son como segundos"
"""
l longitud plataforma
g gombas

d directon (rigth,left) 0 or 1
i 
"""
l,g=map(int,input().split(" "))
moretime=0
for i in range(g):
	p,d=map(int,input().split(" "))
	if d==1:#rigth
		tmptime=l-p
	if d==0:	
		tmptime=p
	#print(tmptime)
	if moretime<tmptime:
		moretime=tmptime
print(moretime)