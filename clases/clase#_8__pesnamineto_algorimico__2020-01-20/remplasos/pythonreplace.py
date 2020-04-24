def añadir(lista,veces):
	uni = u"0x0000000"
	if lista == None :
		lista = str(uni.encode('ascii','ignore'))
	for i in range(veces):
		lista.append(str(uni.encode('ascii','ignore')))
	return lista
def reemplazar(base,reemplazar,replaso):#en la que se va a palabra a reemplazar, palabra a reemplazar,  replaso
	
	primerapos = 0
	ultimapos = 0
	capusla = []
	counter = 0
	length = len(base)
	lbase = list(base)
	lreemplazar = añadir(list(reemplazar),len(base))
	lreplaso = añadir(list(replaso),len(base))
	palabra = ""
	for count,i,j,k in zip(range(len(base)),lbase,lreemplazar,lreplaso):
		print(i,j,k)
		if i == j  :
			#lbase[:i] = k
			primerapos = base.find(j)
			ultimapos = primerapos+len(reemplazar)
			lbase[count] = ""
	#lbase = lbase.pop(lbase[ultimapos:primerapos])
			#primerapos = ((primerapos**2)(**(1/2)))
		elif j in lbase[primerapos:ultimapos]  :
			print(lbase,"ausili")
			lbase.remove(j)

	print(lbase[primerapos:ultimapos],primerapos,ultimapos)
	lbase[primerapos:ultimapos] = replaso
	for string in lbase:
		palabra += string
	return palabra
	"""
			print(i,j,"pasa")
			base.remove(j)
			puesto = count
			base[puesto] = capusla
			for string in base:
			palabra += string	
	"""
	return lbase
base = "no soy capas"
frase = reemplazar(base,"soy","es")
print(frase)

