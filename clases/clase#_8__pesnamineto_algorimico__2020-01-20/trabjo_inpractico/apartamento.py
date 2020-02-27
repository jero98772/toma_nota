import subprocess

apts = 60
for i in range(apts):
	subprocess.run("clear", shell =True)
	print("="*80)
	print("           _           _       _     _                  _              ")
	print("  __ _  __| |_ __ ___ (_)_ __ (_)___| |_ _ __ __ _  ___(_) ___  _ __   ")
	print(" / _` |/ _` | '_ ` _ \| | '_ \| / __| __| '__/ _` |/ __| |/ _ \| '_ \  ")
	print("| (_| | (_| | | | | | | | | | | \__ \ |_| | | (_| | (__| | (_) | | | | ")
	print(" \__,_|\__,_|_| |_| |_|_|_| |_|_|___/\__|_|  \__,_|\___|_|\___/|_| |_| ")
	print("                                                                       ")
	print(" _           _                                                  ")
	print("| |__   ___ | | ___ _ __   __ _ _ __   __ _    __ _ _   _  ___  ")
	print("| '_ \ / _ \| |/ _ \ '_ \ / _` | '_ \ / _` |  / _` | | | |/ _ \ ")
	print("| |_) | (_) | |  __/ | | | (_| | | | | (_| | | (_| | |_| |  __/ ")
	print("|_.__/ \___/|_|\___|_| |_|\__,_|_| |_|\__,_|  \__, |\__,_|\___| ")
	print("                                                 |_|            ")
	print("   ____      _       ")
	print("  / __ \  __| | ___  ")
	print(" / / _` |/ _` |/ _ \ ")
	print("| | (_| | (_| | (_) |")
	print(" \ \__,_|\__,_|\___/ ")
	print("  \____/         ")
	print("="*80)
	residentes = int(input("buenas venimos a hacer un cesnso por parte del edficio nesesisto que me responda las siguietes pregutas \n ¿cuantas personas  en su vivienda viven en el apartamento?:  "))
	if residentes > 0:
		mascota = str(input("tiene alguna especie de animal en su casa domesticada o una mascota \n P) <-- perr@ \n G) <-- gato \n >=>) <-- pez(es) \n O) <-- otra(s) \n responda: "))
		for j in range(residentes):
		    genero = str(input("¿usted es del genero ?\n M) <-- masculino \n F) <-- femenino \n I) <-- indefinido \n 404) <-- no encontrado \n responda: "))
		    edad = int(input("si usted esta vivo a respondido lo anterior con sinceridad respononda esto con la mayor transparencia ¿cuantos años tiene?: "))
		    while not (0 < edad  < 150):
		        print("esto es por el bien comun no ganas nada expto que el gran hermano no tenga tus verderos datos")
		        edad = int(input("si usted esta vivo a respondido lo anterior con sinceridad respononda esto con la mayor transparencia ¿cuantos años tiene?: "))

		    if input("¿si respondio con sinceridad ? \n si) <-- si respondi mayormente con  sinceridad \n no)<-- no perdoname la vida \n responda con cabesa: ").lower() == "no":
		        while not (0 < edad  < 150):
		            print("esto es por el bien comun no ganas nada expto que el gran hermano no tenga tus verderos datos")
		            edad = int(input("si usted esta vivo a respondido lo anterior con sinceridad respononda esto con la mayor transparencia ¿cuantos años tiene? : "))
		
		else :
			print("muy amale por su colaboracion no fue de mucha ayuda")
			input("presione enter")

	else :
		print("corra l) <-- loco  \n f) <-- fantasma \n s) <-- un sueño \n e) <-- exeso de alcohol")