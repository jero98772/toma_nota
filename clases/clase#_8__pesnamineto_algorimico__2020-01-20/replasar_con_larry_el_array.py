def reemplazar(base,reemplazar,replaso):#en la que se va a palabra a reemplazar, palabra a reemplazar,  replaso

	lbase = list(base)
	reemplazar = list(reemplazar)
	capusla = []
	counter = 0
	length = len(base)
	capusla.append(replaso)

	for count,i,j,k in zip(range(len(base)),base,reemplazar,replaso):
		print(i,j,"no")	
		if i == j  :
			print(i,j,"pasa")
			base.remove(j)
			puesto = count
			base[puesto] = capusla
		
	print(*lbase)
base = "en algunos"
frase = reemplazar(base,"algunos","todos")
