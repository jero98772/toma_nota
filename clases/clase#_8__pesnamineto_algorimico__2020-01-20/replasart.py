def reemplazar(base,reemplazar,replaso):#en la que se va a palabra a reemplazar, palabra a reemplazar,  replaso

	lbase = list(base)
	reemplazar = list(reemplazar)
	capusla = []
	counter = 0
	length = len(base)
	capusla.append(replaso)
	uni = u"0x0000000"
	#for count,i in zip(range(len(base)),base):
		#for j,k in zip(reemplazar,replaso):
	#for count in range(length):
			#for i,j,k in zip(lbase,reemplazar,replaso):
	for count,i,j,k in zip(range(length),base,reemplazar,replaso):
		print(i,j,"no")	
		counter += 1
		ultima = base.find(j)

		if i == j :#and len(reemplazar) > counter   :
			lbase[count] = str(uni.encode('ascii','ignore'))
			#lbase.remove(j)
			#print(i,j,"pasa")

			#if count == length :#or count == *length-1 :
	else:
		puesto = count
		print("llegos")
		lbase[ultima] = capusla
		for i in range(len(reemplazar)-1):
			lbase.remove(str(uni.encode('ascii','ignore')))
	"""for count,i,j,k in zip(range(len(base)),base,reemplazar,replaso):
		print(i,j,"no")	
		if i == j  :
			print(i,j,"pasa")
			base.remove(j)
			puesto = count
			base[puesto] = replaso
	"""	
	print(*lbase)
base = "helmepo llego a paris"
frase = reemplazar(base,"helmepo","yo daniel")