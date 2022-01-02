answer=[] 
def permutation(string, i, length):
   if i == length:
        answer.append(''.join(string) )
   else:
       for j in range(i, length):
           string[i], string[j] = string[j], string[i]
           permutation(string, i + 1, length)
           string[i], string[j] = string[j], string[i]
s="1234"
permutation(list(s), 0,4)
print(str(answer))
