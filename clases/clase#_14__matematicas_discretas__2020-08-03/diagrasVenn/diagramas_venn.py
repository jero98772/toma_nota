"""
La Facultad de Ciencias Básicas de la Universidad de Medellín requiere de 30 docentes de cátedra para orientar 14 cursos de Física I (F), 14 de Algebra y Trigonometría (M) y 15 de Sistemas Geométricos (S). El decano al organizar las hojas de vida distribuyo a dichos docentes así: 7 catedráticos para Física I y Algebra y Trigonometría; 4 catedráticos para Física I y Sistemas Geométricos y, 5 catedráticos para Algebra y Trigonometría y Sistemas Geométricos.
Departamento de estadística quiere saber (utilice un diagrama de Venn):
a)¿Cuántos catedráticos orientarán o Física I u orientarán Sistemas Geométricos, pero no Algebra y Trigonometría?
R/4
b)¿Cuántos catedráticos orientaran solamente 2 asignaturas o únicamente Física I o Sistemas geométricos?
R/4
c)¿Cuántos catedráticos si orientaran Sistemas geométricos, pero no Física I entonces, no orientarán Algebra y Trigonometría?
R/2
"""
#proceso de analisis
"""
30 docentes catedra
14 fisica
14  algebra
15 geometria
combinacion
7 fisica y algebra
4 fisica y geometria 
5 algebra y geometria
unicamente por materia
4+7 = 11, 14-11 = 3 profesores que solo dan fisica
7+5 = 12, 14-12 = 2 profesores que solo dan algebra y ...
4+5 = 9, 15-9 = 6 profesores que solo dan geometria
siginificado elementos del conjunto
p profesor catedra
Fp profesor fisica
Mp prfoesor algebra y ...
Sp profesor geometria
FMp profesor de fisica y algebra y ...
FSp profesor de fisica y geometria
MSp profesor de geometria y algebra y ...
FMSp profesor de fisica ,geometria  y algebra y ...
"""
#recuerde usar matplotlib-venn instalelo con "pip install -U matplotlib-venn"
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles
#se reciven parametros como diccionarios {"nombre":cantidad}
def asignatuara(unicaAsignatura,enOtras):
	elementosTotales = []
	elemento = list(unicaAsignatura)[0]
	elementos = list(enOtras)
	for i in range(unicaAsignatura[elemento]):
		elementosTotales.append(elemento)
	for elemento in elementos:
		for i in range(enOtras[elemento]):		
			elementosTotales.append(elemento)
	return elementosTotales
def cantidadDocente(Docentes):
	elemento = list(Docentes)[0]
	cantidad = Docentes[elemento]
	return cantidad

def main():
	fisicadict = {"Fp":3}
	geometriadict = {"Sp":2}
	algebradict = {"Mp":2}
	fiscaYalgebradict = {"FMp":7}
	fiscaYgeometriadict = {"FSp":4}
	geometriaYalegebradict = {"MSp":5}
	todasAsignaturas = {"FMSp":3}
	"""
	fisica = set(asignatuara({"Fp":3},{"FMp":7,"FSp":4}))
	geometria = set(asignatuara({"Mp":2},{"FMp":7,"MSp":5}))
	alegbray = set(asignatuara({"Mp":2},{"FMp":7,"MSp":5}))
	fisica = asignatuara({"Fp":3},{"FMp":7,"FSp":4})
	geometria = asignatuara({"Mp":2},{"FMp":7,"MSp":5})
	alegbray = asignatuara({"Mp":2},{"FMp":7,"MSp":5})
	"""
	venn3(subsets = (cantidadDocente(fisicadict),cantidadDocente(geometriadict),cantidadDocente(fiscaYgeometriadict),cantidadDocente(algebradict),cantidadDocente(fiscaYalgebradict),cantidadDocente(geometriaYalegebradict),cantidadDocente(todasAsignaturas)), set_labels=('fisica', 'geometria','alegbra y ...'))
	plt.show()
main()
