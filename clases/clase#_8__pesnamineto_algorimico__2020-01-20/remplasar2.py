"""
Implemente una función remplazar que reciba un string base, un string objetivo y el nuevo string y retorne otro string donde el string objetivo fue reemplazado por el nuevo string.

El encabezado de la función puede ser así:

def reemplazar(base, objetivo, nuevo):
"""
def reemplazar(base,reemplazar,replaso):#en la que se va a palabra a reemplazar, palabra a reemplazar,  replaso
	reemplazar = list(reemplazar+" ")
	replaso = list(replaso+" ")	
	palabra = ""
	if len(reemplazar)<len(replaso):
		length = len(base)-len(reemplazar)+len(replaso)
		#extraspaces = len(reemplazar)+len(replaso)//2 era una idea para que quedaran mas espacios y poder meter las palabras
		#extra = extraspaces*" "+base+" "*extraspaces
		#print("extra",len(extra))
		base = list(base)

		print("<",length)
		for count in range(length*10):
			for i,j,k in zip(base,reemplazar,replaso):

				print(i,j,k)
				if i == j :

					base[count] = k
					
					print(i,j,k,"se cumple")

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
base = "no cuenta espacios"
frase = reemplazar(base,"no","tambien")
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
