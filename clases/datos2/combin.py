from itertools import  combinations,permutations
letras = "abcdefghijklmnopqrstuvwxyz"

a=permutations(letras,7) 
print(list(a))
#y = [' '.join(i) for i in a]  
#y=permutations("abc",3)
#print(list(y))