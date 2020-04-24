def reemplazar(base,reemplazar,replaso):#en la que se va a palabra a reemplazar, palabra a reemplazar,  replaso

	lbase = list(base)
	reemplazar = list(reemplazar)
	capusla = []
	counter = 0
	length = len(base)
	capusla.append(replaso)
	uni = u"0x0000000"
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
	print(*lbase)
base = "helmepo llego a paris"
frase = reemplazar(base,"paris","italia")
