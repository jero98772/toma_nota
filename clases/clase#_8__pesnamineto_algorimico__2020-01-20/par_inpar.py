entrada = int(input(" ponga un numero natural par o inpar  "))
if entrada > 0:
    print("es un numero natural que es :")
    if entrada % 2 == 0:
        print("es par")
    else:
        print("es inpar")
