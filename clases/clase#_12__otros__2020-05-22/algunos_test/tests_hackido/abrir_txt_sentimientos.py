from random import randrange
feels_list = []
with open('diccionario_sentimientos.txt', 'r') as feels:
    for line in feels.readlines():
        feels_list.append(str(line).replace("\n",""))
print(feels_list,feels_list.index("agresivo"))
rnd = randrange(len(feels_list))
print(feels_list[rnd ])

