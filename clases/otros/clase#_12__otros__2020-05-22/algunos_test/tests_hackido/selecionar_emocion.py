#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
selecionar_emocion - 2020 - por jero98772
selecionar_emocion - 2020 - by jero98772
"""
#sentimientos = ["trsitesa","misterio","estres","rabia","extraño","alegia","felizidad","ira"] 
loquesiento = ["trsiteza","misterio","estres","rabia","extraño","estres","trsiteza","misterio","felicidad","estres","rabia","extraño","estres","trsiteza","misterio","felicidad"]
sentimientos = {i:loquesiento.count(i) for i in loquesiento}
print(sentimientos)
predominante = ""
masveces = 0
for i,j in zip(sentimientos.keys(),sentimientos.values()):
	if masveces < j:
		masveces = j
		predominante = i
print(predominante)
print(masveces)
#puede servir para algo en hackido

