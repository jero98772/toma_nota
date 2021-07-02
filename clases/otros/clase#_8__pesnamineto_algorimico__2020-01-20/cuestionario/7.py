# -*- coding: utf-8 -*-
#!/usr/bin/env python 

def alternar_mayuscula_minuscula(nombre):
    alternado = ""
    for i in range(len(nombre)):
        if i %2 == 0:
            alternado += nombre[i].upper()


        else:
            alternado += nombre[i].lower()


    return alternado
a=alternar_mayuscula_minuscula("AnDrÉs")
print(a)
