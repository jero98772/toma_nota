def xs(txt,i,size,newtxt,chararcter="x"):
    if i<size:
        if txt[i]==chararcter:
            return xs(txt,i+1,size,newtxt+"y",chararcter)
        else:
            return xs(txt,i+1,size,newtxt+txt[i],chararcter)
    else:
        return newtxt
txt=input()
print(xs(txt,0,len(txt),"","x"))