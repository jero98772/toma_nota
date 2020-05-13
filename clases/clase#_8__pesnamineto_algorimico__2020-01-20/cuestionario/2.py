#Para el siguiente algoritmo, complete la prueba de escritorio asumiendo un valor de n = 8. Al final indique cuál sería el valor de la variable d
n = int(input("Ingrese Número: "))
c = 0
for i in range(1, n):
    print(i,c,i % 3==0)
#los que son dividos por 3
    if i % 3 == 0:
        c += 1

d = (100 * c) // n
print(d)
