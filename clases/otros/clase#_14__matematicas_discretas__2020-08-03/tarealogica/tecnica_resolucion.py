#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
tecnica_resolucion - 2020 - por jero98772
tecnica_resolucion - 2020 - by jero98772
"""
VOF = input("ingrese las V y F")
try: 
	VOF = VOF
except:  
	VOF = "VVFFVVVVFFVVVVVVVVFFVVVVFFVVVVVV"
if not VOF:
	VOF = "VVFFVVVVFFVVVVVVVVFFVVVVFFVVVVVV"
V = True
F = False
for i,j in zip(VOF,range(len(VOF))) :
	if j == 0:
		proposion = eval(i)
	else:				
		proposion = not (proposion and eval(i))
	print(proposion,i)  	

