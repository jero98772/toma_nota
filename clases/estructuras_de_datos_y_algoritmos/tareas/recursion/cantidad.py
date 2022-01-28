def xs(txt,i,size,x,chararcter="x"):
    if i<size:
        if txt[i]==chararcter:
            return xs(txt,i+1,size,x+1,chararcter)
        else:
            return xs(txt,i+1,size,x,chararcter)
    else:
        print(x)
        return x
txt=input()
print(xs(txt,0,len(txt),0,"x"))