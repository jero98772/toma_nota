def reemplazar(base,reemplazar,replaso):#en la que se va a palabra a reemplazar, palabra a reemplazar,  replaso
	reemplazar = list(reemplazar)

	palabra = ""
	frase = ""
	pos = []
	capusla = []
	counter = 0
	lbase = list(base)
	length = len(base)
	capusla.append(replaso)
	uni = u"0x0000000"
	if len(reemplazar)<len(replaso):
		length = len(base)-len(reemplazar)+len(replaso)
		#extraspaces = len(reemplazar)+len(replaso)//2 era una idea para que quedaran mas espacios y poder meter las palabras
		#extra = extraspaces*" "+base+" "*extraspaces
		#print("extra",len(extra))
		print("<",length)
		counter = 0
		

		for count,i,j,k in zip(range(length),base,reemplazar,replaso):

			counter += 1
			ultima = base.find(j)

			if i == j :#and len(reemplazar) > counter   :
				lbase[count] = str(uni.encode('ascii','ignore'))

		else:
			puesto = count
			print("llegos")
			lbase[ultima] = replaso
			
			for i in range(len(reemplazar)-1):
				lbase.remove(str(uni.encode('ascii','ignore')))
		print(puesto)
		"""for z in range(len(lbase)):
			for x,y in zip(lbase,lbase[ultima]):
				print(x,y,z)
				if z == puesto:
					lbase.remove(lbase[ultima])
					palabra += str(lbase[ultima])
					print("a")
				else:
					palabra += y
					print("b")
				break"""
		print(lbase)
		print(*lbase)
	else:
		#funciona
		length = len(base)+(len(replaso)-len(reemplazar))
		print(">",length)
		extraspaces = len(reemplazar)+len(replaso)
		base = list(base)
		#aqui podria poner si falla para una general
		for i,count in zip(base,range(length*10)):
			for j,k in zip(reemplazar,replaso):
				print(i,j,k)
				if i == j :
					base[count] = k

	
		print(base[:length])
		for string in base[:length]:
			palabra += string

		return palabra
# hacer una funcion como replace
#base= "oma y opa"
base = "no las perras cuenta espacios"
frase = reemplazar(base,"no las perras","tambien")
#frase = reemplazar(base,"m","p")
#frase = reemplazar("no funciona con espacios","no","tambien")
print("frase original",base)
replasada=base.replace("no","tambien")
print("como deveria ser",replasada, len(replasada))
print("como es",frase)


"""
el problema parese estar base countk
combinaciones con los for
i,j,k,c fail
j,k,c,i fail
k,c,i,j fail
c,i,j,k fail
c,ij,k original word
ij,k,c  original word
k,c,ij
los for
#for i,j,k in zip(base,reemplazar,replaso):
#for j in reemplazar:
#for i in base :
#for i,j in zip(base,reemplazar):
#for count  in range(len(base)):
#for j in reemplazar:
#for i,k in zip(base,replaso):
#for count,j  in zip(range(len(base)),reemplazar):
#for i,k in zip(base,replaso):

funciona mas o menos con
	for i,count in zip(base,range(length*10)):
		for j,k in zip(reemplazar,replaso):
			print(i,j,k)
			if i == j :

				base[count] = k

"""
