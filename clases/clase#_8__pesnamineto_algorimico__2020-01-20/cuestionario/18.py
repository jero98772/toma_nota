def orden(num1, num2):
    if num1 >= num2:
        menor = num2
        mayor = num1
    else:
        menor = num1
        mayor = num2
    return menor, mayor
print(orden(5, 3))