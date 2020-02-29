dinero = int(input("su dinero a repartir dividir en grandes cantidades"))
contraMenuda = dinero 
if contraMenuda > 0:

    veces50000 = contraMenuda // 50000
    contraMenuda  = contraMenuda % 50000

    veces20000 = contraMenuda // 20000
    contraMenuda = contraMenuda % 20000

    veces10000 = contraMenuda // 10000
    contraMenuda  = contraMenuda % 10000

    veces5000 = contraMenuda // 5000
    contraMenuda = contraMenuda % 5000
    
    veces2000 = contraMenuda // 2000
    contraMenuda  = contraMenuda % 2000

    veces1000 = contraMenuda // 1000
    contraMenuda = contraMenuda % 1000

    veces500 = contraMenuda // 500
    contraMenuda  = contraMenuda % 500

    veces200 = contraMenuda // 200
    contraMenuda = contraMenuda % 200

    veces100 = contraMenuda // 100
    contraMenuda  = contraMenuda % 100

    veces50 = contraMenuda // 50
    contraMenuda = contraMenuda % 50

    veces20 = contraMenuda // 20
    contraMenuda  = contraMenuda % 20

    veces10 = contraMenuda // 10
    contraMenuda = contraMenuda % 10

    veces5 = contraMenuda // 5
    contraMenuda  = contraMenuda % 5

    veces1 = contraMenuda // 1
    contraMenuda = contraMenuda % 1

    print(f"{veces50000} veces el billete de 50000")
    print(f"{veces20000} veces el billete de 20000")
    print(f"{veces10000} veces el billete de 10000")
    print(f"{veces5000} veces el billete de 5000")
    print(f"{veces2000} veces el billete de 2000")
    print(f"{veces1000} veces el billete de 1000")
    print(f"{veces500} veces el billete de 500")
    print(f"{veces200} veces el billete de 200")
    print(f"{veces100} veces el billete de 100")
    print(f"{veces50} veces el billete de 50")
    print(f"{veces20} veces el billete de 20")
    print(f"{veces10} veces el billete de 10")
    print(f"{veces5} veces el billete de 5")
    print(f"{veces1} veces el billete de 1")
