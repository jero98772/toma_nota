import heapq
def getprob(l)->dict:
    """
    getprob(l)->dict
    get proabiliti of ocurrences in list, can be usen in list and strings
    """
    clearlist=list(set(l))
    prob={}
    for i in clearlist:
        prob[str(i)]=l.count(i)/len(l)
    return prob

def code(frequency):
    #weight, symbol, code
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        for value in low[1:]:
            value[1] = '0' + value[1]
        for value in high[1:]:
            value[1] = '1' +value[1]
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
def getdict(huff):
    d={}
    for i in huff:
        d[i[0]]=i[1]#char,code
    return d
def encode(txt,d):
    newstr=""
    for i in txt:
        newstr+=d[i]
    return newstr

def decode(txt,d):
    newstr=""
    word=""
    tmp=None
    oc=0
    for i in txt:
        word+=i
        for ii in d.keys():
            if word in ii:
                oc+=1
                word=ii
        if oc==1:
            newstr+=word
    return newstr
#recorriendo el arbol

def main():
    string=input("Enter the string to codifie:\n")
    frequency=getprob(string)
    huff = code(frequency)
    d=getdict(huff)
    #print("character".ljust(10) + "Weight".ljust(10) + "Huffman Code")
    #for i in huff:
    #    prob=round(float(frequency[i[0]]),5)
    #    print(i[0].ljust(10) + str(prob).ljust(10) + i[1])

    inp=input("[D]Decode or [E]Encode, print [C]code\n").lower()
    if inp=="d" or inp=="decode" :
        #string=input("Enter the string to decode:")
        dec=decode(string,d)
        print(dec)

    if inp=="e" or inp=="encode":
        #string=input("Enter the string to encoded:")
        enc=encode(string,d)
        print(enc)
    if inp=="c" or inp=="code":
        print("character".ljust(10) + "Weight".ljust(10) + "Huffman Code")
        for i in huff:
            prob=round(float(frequency[i[0]]),5)
            print(i[0].ljust(10) + str(prob).ljust(10) + i[1])
if __name__ == '__main__':
    main()
