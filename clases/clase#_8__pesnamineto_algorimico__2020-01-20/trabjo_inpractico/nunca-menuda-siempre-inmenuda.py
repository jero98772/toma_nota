dinero = int(input("su dinero a repartir dividir en grandes cantidades"))
contraMenuda = dinero 
if contraMenuda > 0:
    contraMenuda  = contraMenuda % 50000
    veces50000 = contraMenuda // 50000

    contraMenuda = contraMenuda % 20000
    veces20000 = contraMenuda // 20000
