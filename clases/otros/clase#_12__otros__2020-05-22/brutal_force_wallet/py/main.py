from itertools import product
import subprocess


#multitreading
#brutal force

def brutalforceGen(chars):
    for length in range(1, 6): # only do lengths of 1 + 2
        to_attempt = product(chars, repeat=length)
        for attempt in to_attempt:
            print(''.join(attempt))
#try
def doSomthing(value):
    out=subprocess.run("cat password", stdout=subprocess.PIPE, universal_newlines=True,shell=True)
    if str(value)==str(out.stdout):
        print("value is: \n\t"+value)
        exit()
#generate dict
#save
def main():
    CHARS="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    brutalforceGen()
if __name__=="__main__":
    main()
