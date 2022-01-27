def factorial(n : int) -> int:
    if n<=0:
        return n
    else:
        return n*factorial(n)

def main():
    n = int(input())
    print(factorial(n))
    
main()