from collections import deque
def binarios(n):
    lista_res=deque()
    cola_q=deque()
    cola_q.appendleft("1")
    for i in range (0,n):
        el_elemento_que_estaba_de_primero_en_la_cola = cola_q.pop()
        lista_res.append(el_elemento_que_estaba_de_primero_en_la_cola)
        cola_q.appendleft(el_elemento_que_estaba_de_primero_en_la_cola+"0")
        cola_q.appendleft(el_elemento_que_estaba_de_primero_en_la_cola+"1")     #lista_res.append(cola_q)
    return lista_res
"""
from collections import deque
def binarios(n):
    lista_res=deque()
    cola_q=deque()
    cola_q.appendleft("1")
    lista_res.append("1")
    for i in range (2,n):
        lista_res.append(bin(i))
        #cola_q.appendleft("1")
        #cola_q.pop()
        #cola_q.appendleft(cola_q.pop())
        #lista_res.append(cola_q)
    return lista_res
"""    
print(list(binarios(int(input()))))
