dia = int(input("dia nacimiento \t"))
mes = int(input("mes el cual nacio \t"))
años = int(input("año de nacimiento  \t"))
#entradas del usiario
def eddad(dia,mes,años):
    #sistema de medicion
    D=30
    M=12
    A=2020
    print ("fecha es ",dia,"dia \t",mes,"mes \t",años,"año")
    #dias de 2020
    añosdias=(A*M*D)
    #dias de años//22
    AÑOSdias=(años*M*D)
    #dias de meses//9
    MESESdias=(mes*D)
    eddad_dias=añosdias-AÑOSdias-MESESdias-dia
    eddad=eddad_dias/ (D*M)
    print ("eddad en dias",eddad_dias,"usted tiene ", eddad ,"años")# ,añosdias,"la cantiad del siglo")
eddad(dia,mes,años)


