#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
def writetxt(name,content):
	"""
	writetxt(name,content) , write in txt file something  and create if file dont exist
	"""
	content =str(content)
	with open(name+".txt", 'w') as file:
		file.write(content)
		file.close()
def guardarFrase():
    writetxt("frase.txt",input())
