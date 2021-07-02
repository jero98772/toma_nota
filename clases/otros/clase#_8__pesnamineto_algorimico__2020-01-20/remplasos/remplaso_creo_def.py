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
base = "algunos queremos anarquia"
frase = reemplazar(base,"algunos","todos")
