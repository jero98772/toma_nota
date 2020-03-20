#try:     
def primos(num):
    if num > 0:
        for i in range(2,num-1):
            if num % i== 0 :
                break
        else :
            return num
                
def gemelos(num,num2):
    if num+2 == num2 or num == num2+2:
        return num, num2 ,True
    else :
        return False
def primos_gemelos(num,num2):
    numero , numero2 ,siOno= gemelos(primos(num),primos(num2))
    if siOno:
        text = "son numeros primos gemelos"
    return numero, numero2 ,text
print(primos_gemelos(7,5))
#except:
    #print("no es un numero gemolo primo")