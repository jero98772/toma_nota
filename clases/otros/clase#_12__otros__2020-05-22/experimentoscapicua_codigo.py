def esCapicua(num):
    num = list(str(num))
    count = 0
    check = []
    boolcapicua = False
    if len(num) % 2 == 0:
        indice = int(len(num)/2)
        for i in range(indice):
           if not num[-i] == num[:i]:
               return False
               #check.append(True)
        else:
            return True
    else: 
        indice = int((len(num)-1)/2)
        for i in range(indice):
           if num[-i] == num[:i]:
               check.append(True)
    for i in check:
       if not i:
          return False
          break 
numtest = [2,3,5,7,11,13,17,19,23,29,101, 103,107,109,113]
#return len(numtest)
print(esCapicua(565))
