def habilitarProceso(persona , cursos):
	refcursosstr = "\n"
	for i,j in zip(cursos,range(len(cursos))):
		refcursosstr += str(j)+str(i)+"\n"	
	msg = "hola "+str(persona) + "puedes hacceder a estos cursos" + str (cursos)+ "puedes (en este caso escoger 1 por ahora) introdice el numero  "+refcursosstr
	curso = int(input(msg)) 
	hoario = input("en que hoario?") 
	return curso , hoario	
class matricula():
	def __init__(self,estudiante,cursosDisponibles):
		self.cursosDisponibles = cursosDisponibles
		self.estudiante = estudiante 
	def estaActivo(self,actividadReciente):
		self.actividadReciente = actividadReciente
		if self.actividadReciente :return habilitarProceso(self.estudiante,self.cursosDisponibles)
		else : return "no te puedes matricular o te falta hacer algo"
	def cambiarCurso(self,nuevoCurso):
		self.nuevoCurso = nuevoCurso
		return self.nuevoCurso
	def cancelarCurso(self):
		self.nuevoCurso = ""
		return self.nuevoCurso 
	def cambiarHorario(self,nuevoHorario):
		self.nuevoHorario = nuevoHorario		
		return self.nuevoHorario
	def cacelarTodo(self):
		self.actividadReciente = False
		return self.actividadReciente 
cursos = ["magia","pocimas","hechisos","matematicas","quimica","fisica"]
m = matricula("algun estudiante",cursos)
print(m.estaActivo(True),"estaActivo")
print(m.cambiarCurso("magia"),"cambiarCurso")
print(m.cambiarHorario(cursos[1]),"cambiarHorario")
print(m.cancelarCurso(),"cancelarCurso")
print(m.cacelarTodo(),"cacelarTodo")
print(m.cambiarCurso("magia"),"cambiarCurso")
