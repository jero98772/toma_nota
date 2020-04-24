base = "no cuenta espacios"
def reemplaso(base,posreemplazar,replaso):
	base = base.split(" ")
	base[posreemplazar] = replaso
	string = " ".join(base)
	return string
al = reemplaso(base,0,"tambien")
print(al)	
