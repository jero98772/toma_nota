def getprob(words):
    prob={}
    for i in words:
        #print(i)
        if i in prob:
            prob[i]+=1
        else:
            prob[i]=1
    return prob
def assign_code(nodes, label, result, prefix = ''):    
    childs = nodes[label]     
    tree = {}
    if len(childs) == 2:
        tree['0'] = assign_code(nodes, childs[0], result, prefix+'0')
        tree['1'] = assign_code(nodes, childs[1], result, prefix+'1')     
        return tree
    else:
        result[label] = prefix
        return label
 
def Huffman_code(vals):    
    nodes = {}
    for n in vals.keys():
        nodes[n] = []
    while len(vals) > 1:
        s_vals = sorted(vals.items(), key=lambda x:x[1]) 
        a1 = s_vals[0][0]
        a2 = s_vals[1][0]
        vals[a1+a2] = vals.pop(a1) + vals.pop(a2)
        nodes[a1+a2] = [a1, a2]        
    code = {}
    root = a1+a2
    tree = {}
    tree = assign_code(nodes, root, code)  
    return code, tree
    
def encode(text,code):
    encoded = ''.join([code[t] for t in text])
    return encoded   
def decode(encoded,tree):
    decoded = []
    i = 0
    while i < len(encoded):
        ch = encoded[i]  
        act = tree[ch]
        while not isinstance(act, str):
            i += 1
            ch = encoded[i]  
            act = act[ch]        
        decoded.append(act)          
        i += 1
    return ''.join(decoded)

def main():
    inp=input("[D]Decode or [E]Encode, print [C]code\n").lower()
    string=input("Enter the string:\n")
    frequency=getprob(string)
    code, tree = Huffman_code(frequency)
    if inp=="d" or inp=="decode" :
        frequency=eval(input("input your frequency characters as dict (example: {a:2,b:2})"))
        code, tree = Huffman_code(frequency)
        dec=decode(string,tree)
        print(dec)
    if inp=="e" or inp=="encode":
        frequency=getprob(string)
        code, tree = Huffman_code(frequency.copy())
        #python pasa el diccionario por referencia por eso usamos copy para no dañar el diccionario
        print(code)
        enc=encode(string,code)
        print(enc)
        print("save frequency:")
        print(frequency)
    if inp=="c" or inp=="code":
        frequency=getprob(string)
        code, tree = Huffman_code(frequency.copy())
        print("character".ljust(10) + ":".ljust(10) + "Huffman Code")
        for k in code:
            print(k,"  :  ",str(code[k]))
if __name__ == '__main__':
    main()