from itertools import product
import subprocess
def readtxtline(name):
	with open(name, 'r') as file:
		return str(file.readline())

def doSomthing(value):
   # subprocess.run("cat password.txt",shell=True)
    out=subprocess.run("cat password", stdout=subprocess.PIPE, universal_newlines=True,shell=True)#password have 1234
    if str(value)==str(out.stdout):
        print("value is: \n\t"+value)
        exit()

def brutalforceGen(chars,star=0,end=3):
    for length in range(star,end): # only do lengths of 1 + 2
        to_attempt = product(chars, repeat=length)
        for attempt in to_attempt:
            attemptStr=''.join(attempt)
            doSomthing(attemptStr)
            print(attemptStr)

def main():
    #CHARS="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    CHARS="aeiou"
    brutalforceGen(CHARS)
if __name__=="__main__":
    main()