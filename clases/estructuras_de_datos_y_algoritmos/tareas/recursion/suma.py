def sumar(n:int)->int:
    if n<1:
    	return 0
    else:
    	return n+sumar(n-1)

def main():
    n=int(input())
    print(sumar(n))
    
main()