class barco:
	def __init__(self,color = "azul", bandera = "panameña", tonelaje =3000, maxvelkmh = 50 ,matricula = "pmz876" ):
		self.color = color
		self.bandera = bandera 
		self.tonelaje = tonelaje
		self.maxvelkmh = maxvelkmh
		self.matricula = matricula 
	def modelamiento(self):
		modelo = "hay un barco de color "+str(self.color)+" que representa su pais con su bandera "+str(self.bandera ) + " y impotrtante para el trasporte es su tonelaje  "+ str(self.tonelaje)+" es te barco como otros es lento  a comparacion de un avion y su respectiva velociadad es de "+ str(self.maxvelkmh) + " y si algo hace identificar este barco y por lo que se distinge es su matricula es "+ str(self.matricula)
		return modelo
def main():
	barcoPredetermina = barco()
	print(barcoPredetermina.modelamiento())
main()
