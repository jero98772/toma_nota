def caracter(cadena):
    chars={}
    for i in cadena:
        print(i)
        if i in chars:
            chars[i]+=1
            if chars[i]==2:
                return i
        else:
            chars[i]=1
            