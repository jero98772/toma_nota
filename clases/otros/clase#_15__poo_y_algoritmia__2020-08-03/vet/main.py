from veterinaria import mascota ,diagnostico,propietario
from rich import print
peso = 373
m = mascota("pez",10,peso)
print(m.tipoMedeicacion(),"tipo mascota")
mensaje,dosis = m.tipoMedeicacion()
print(dosis)
print(mensaje)
print(m.cantiadMediacar(),"cantidad")
d = diagnostico("mañana","alguna descripcion")
print(d.resumen(),"resumen")
p = propietario("sin nombre","la esquina",312000000000,"anonimo@hidenmail.onion")
pagar1 = p.valorpagar("pez",peso)
pagar2 = p.valorPagarCantiad(dosis,peso)
print(pagar1[0],pagar1[1])
print(pagar2[0],pagar2[1])