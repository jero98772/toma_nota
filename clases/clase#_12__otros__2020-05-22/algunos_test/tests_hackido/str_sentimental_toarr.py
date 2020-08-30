#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
str_sentimental_toarr - 2020 - por jero98772
str_sentimental_toarr - 2020 - by jero98772
"""
sentimeintos = """*** estres
*** Tristeza
*** depresión 
*** ansiedad
*** miedo
*** Fobia
*** Llanto frecuente
*** Sentimientos de inferioridad 
*** ira
*** agresividad
*** ideación suicida
*** Alegria 
*** felicidad
*** emoción
*** Amor
*** odio
*** paz interior
*** armonia
*** intranquilidad
*** Amargado
*** engreido
*** desconocimiento
*** conocimiento
*** incomprension
*** compresnion
*** extraño
*** timidez
*** aislarse
*** preocupado
*** aislado
*** soledad
*** intmidado
*** agresion
"""
larrySentimental = []
sentimiento = ""
sentimeintos = sentimeintos.replace("*** ","-")
sentimeintos = sentimeintos.replace("\n","")
for i in sentimeintos:
	if i == "-":
		larrySentimental.append(sentimiento)
		sentimiento = ""
	elif i == 0:
		pass
	else :
		sentimiento += i
print(larrySentimental , len(larrySentimental ))
#un log como ['estres', 'Tristeza', 'depresión ', 'ansiedad', 'miedo', 'Fobia', 'Llanto frecuente', 'Sentimientos de inferioridad ', 'ira', 'agresividad', 'ideación suicida', 'Alegria ', 'felicidad', 'emoción', 'Amor', 'odio', 'paz interior', 'armonia', 'intranquilidad', 'Amargado', 'engreido', 'desconocimiento', 'conocimiento', 'incomprension', 'compresnion', 'extraño', 'timidez', 'aislarse', 'preocupado', 'aislado', 'soledad', 'intmidado']

