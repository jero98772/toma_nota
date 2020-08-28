#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
hackido - 2020 - por jero98772
hackido - 2020 - by jero98772
"""
def contraseñaSegura(password):
	haynumeros = False
	hayletras = False
	haysimbolos = False
	for i in password:
		try:
			if type(int(i)) == type(0):
				print("numeors ok")
				haynumeros = True
			elif type(str(i)) == type(""):
				print("letras ok")
				hayletras = True
		except:
			print("simbolos ok")
			haysimbolos = True
	if haysimbolos and hayletras and haynumeros:
		return True
	else:
		return False

def contraseñaSegura2(password):
	haynumeros = False
	hayletras = False
	haysimbolos = False
	numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for i in password:
		try:
			if i in numeros:
				print("numeors ok")
				haynumeros = True
			elif i in letras:
				print("letras ok")
				hayletras = True
			else:
				if type(int(i)) == type(0):
					print("numeors ok")
					haynumeros = True
				elif type(str(i)) == type(""):
					print("letras ok")
					hayletras = True				
		except:
			print("simbolos ok")
			haysimbolos = True
	if haysimbolos and hayletras and haynumeros:
		return True
	else:
		return False
pwd = input("passowrd con simbolos , txto, numeros\n")
print(contraseñaSegura(pwd))
print("funcdion2")
print(contraseñaSegura2(pwd))
