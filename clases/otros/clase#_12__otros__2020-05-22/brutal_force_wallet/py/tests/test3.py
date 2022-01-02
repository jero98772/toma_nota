from itertools import product
import subprocess
def readtxtline(name):
	with open(name, 'r') as file:
		return str(file.readline())

def doSomthing(value):
   # subprocess.run("cat password.txt",shell=True)
    out=subprocess.run("cat password", stdout=subprocess.PIPE, universal_newlines=True,shell=True)
    if str(value)==str(out.stdout):
        print("value is: \n\t"+value)
        exit()

def brutalforceGen(chars):
    for length in range(1, 6): # only do lengths of 1 + 2
        to_attempt = product(chars, repeat=length)
        for attempt in to_attempt:
            attemptStr=''.join(attempt)
            doSomthing(attemptStr)
            print(attemptStr)

def main():
    #CHARS="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    CHARS="123456789"
    brutalforceGen(CHARS)

main()
