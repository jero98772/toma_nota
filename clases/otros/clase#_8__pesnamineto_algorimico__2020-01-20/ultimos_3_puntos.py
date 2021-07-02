#=======================Ejercicio 11=======================#

"""Escribir una función que calcule el máximo común divisor de dos números y otra
que calcule el mínimo común múltiplo."""
num1 = 1
num2 = 8
num2
#mcd
mcm = lambda num1, num2:num1 * num2/ mcd(num1, num2)
def mcd(num1, num2):
    resto = 0
    while(num2 > 0):
        resto = num2
        num2 = num1 % num2
        num1 = resto
    return num1
#para verificar mas facil
def descomponer(*num):
    numeros = []
    mayor = 0
    num = list(num)
    for i in num:
        if i > mayor:
            mayor = i
        print("\n","///"*5,"\n")
        for mcd in range(1,mayor+1):
            if  i%mcd == 0 :
                print("=="*5)
                print(mcd)
                numeros.append(mcd)
    else:
        print("\n","///"*5,"\n")
descomponer(num1,num2)
print("\n","///"*5,"\n",mcd(num1,num2))
print("\n","///"*5,"\n",mcm(num1,num2))


#=======================Ejercicio 9=======================#
"""

Escribir una función que calcule el total de una factura tras aplicarle el IVA. La
función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver
el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA,
deberá aplicar un 21%."""

iva = lambda precio,porcentajeiva =21:precio*((porcentajeiva*0.01)+1) 

print(iva(5000,9))
#=======================Ejercicio 10=======================#

"""
Escribir una función que calcule el área de un círculo y otra que calcule el volumen
de un cilindro usando la primera función."""
area = lambda r:3.14159265359*(r**2)
volcilindro = lambda altura,area :area*altura
    
print(volcilindro(150,area(50)))
