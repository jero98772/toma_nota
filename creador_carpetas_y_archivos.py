import numpy as np
import os
import datetime
import time
import subprocess
#importo las libererias
hoy=datetime.datetime.now().strftime('%Y-%m-%d')
class tema_clase:
	def tema_clase():
		tema_clase =str(input(" las palabras no pueden ir separado por espacios por que creera que es otro 'comando' ni simbolos \n tema para trabajar en clase: \n  "))
		if tema_clase=="":
			tema_clase= "tema_clase"
			return tema_clase
		return tema_clase
directorio= "clases"
class si_el_archivo_existe:
	""" defino la clase"""
	def si_el_archivo_existe():
		""" defino la funcion"""
		numero_de_la_clase=1
		nombre ="clase#_"
#variables

		for the_file in os.listdir(directorio):
			"""recorrro el diectorio"""
			"""el for convierte los archivos en elementos de una lista que se puden contar individualmente""" 
			numero_de_carpetas=len(os.listdir(directorio))

			numero_de_carpetas+=0
			print(numero_de_carpetas)
			if not  os.walk(the_file) in os.listdir(directorio) :

				while numero_de_carpetas >= numero_de_carpetas:


					numero_de_carpetas+=0
					nombre_numero_y_asignatura=nombre+str(numero_de_carpetas)+"__"+str(tema_clase)+"__"+str(hoy)								
					print(nombre_numero_y_asignatura)
					direccion=directorio+"/"+nombre_numero_y_asignatura
					os.mkdir(direccion)
					return direccion

	
class setup:
	def crear_carpetas_inicales():
		print(directorio)
		if not os.path.exists(directorio):
			os.mkdir(directorio)
			numero_de_carpetas=len(os.listdir(directorio))
			print(numero_de_carpetas)
			if numero_de_carpetas >=0:
				carpeta_vacia="/clase#_"+str(numero_de_carpetas)+"sin_importancia"+str(hoy)
				os.mkdir(directorio+"/"+carpeta_vacia)

setup.crear_carpetas_inicales()
tema_clase=tema_clase.tema_clase()
class 	crear_contenido:
	def crear_contenido():
		nombre=si_el_archivo_existe.si_el_archivo_existe()
		veces_apoyo=eval(input("cantidad de imagenes para tener apoyo visual\n"))
		for i  in range(veces_apoyo):
			comado_kolourpaint=str("touch "+str(nombre)+"/"+str(tema_clase)+"_dibujo"+str(i)+".jpg")
			subprocess.run(str(comado_kolourpaint) , shell=True)
		
		comado_org=str("touch "+str(nombre)+"/"+str(tema_clase)+"_notebook.org")
		subprocess.run(str(comado_org) , shell=True)

		comado_codigo=str("touch "+str(nombre)+"/"+str(tema_clase)+"_codigo.py")
		subprocess.run(str(comado_codigo) , shell=True)
crear_contenido.crear_contenido()
