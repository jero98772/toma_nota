count1=0
count2=0
txtpass=[]
CHARS="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
#iters=txt
def main():
    while True:
        for i in range(len(txtpass)):
            for  ii in range(len(CHARS)):
                print(len(txtpass))
                txtpass[i]=CHARS[ii]
                print(txtpass)
                doTry("".join(txtpass))
            print(len(txtpass),txtpass)
        txtpass.append("")
def observate():
    import time
    time.sleep(0.005);
def doTry(word):
    print(word)
    observate()
main()

#base 58, cada 58*ii nums concatena un nuevo numero , lo añade a un array,los avlores a añadir en el array son numeros, el valor maximo es 58
