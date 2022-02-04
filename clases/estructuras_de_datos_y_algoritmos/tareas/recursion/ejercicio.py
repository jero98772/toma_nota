def palindrome(s):
 size2=len(s)
 return palindromeAux(s,0,size2-1,size2)
def palindromeAux(s,i,ii,size):
  if i==size and ii==0:return True
  else:
   #print(s[i]==s[size-ii],i,ii,i==size and ii==0)
   print(i,ii)
   #print(s[i],s[ii])
   if s[i]==s[ii]:palindromeAux(s,i+1,ii-1,size)
   else:return False
def main():
 s=input()
 print(palindrome(s))
main()