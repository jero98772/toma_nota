def comprobarVida(bichos):
  if(bichos[0] == 0  and bichos[1] == 0 and bichos[2] == 0 and bichos[3] == 0 ):
    print("Felicitaciones salvaste la producción de papas")    
    return True
  else: 
    return False
def menu(bichos):
  mostrar(bichos)
  print("-- Ingrese --")
  print(" 1) Para disparar a un bicho...")
  print(" 2) Lanzar pesticida...")
  print(" 3) Invocar viento de guadalupe...")
  print(" 4) Lluvia acida...")
  print(" 5) Frase tia...")
  print(" 0) salir del juego")
def mostrar (bichos):
  print("-------")
  print(str(bichos[0])+"|"+str(bichos[1]))
  print("-------")
  print(str(bichos[2])+"|"+str(bichos[3]))
def disparar(bichos):
    posicionADisparar = int(input("Ingrese la posición a disparar (0,1,2 ó 3):"))
    bichos [posicionADisparar] =validarVida(bichos[posicionADisparar]-5)
def validarVida(bichoVida):
  if(bichoVida < 0):
    bichoVida=0 
  return bichoVida
def disparar(bichos):
    posicionADisparar = int(input("Ingrese la posición a disparar (0,1,2 ó 3):"))
    bichos [posicionADisparar] = bichos [posicionADisparar]-5
def pesticidas(bichos):
  i=0
  while i<4:
    bichos[i]=bichos[i]/2
    i+=1
def lluviaAcida(bichos):
  posicionALanzar = int(input("Ingrese la posición a disparar (0,1,2 ó 3):"))
  bichos [posicionALanzar] = 0
def vientoDeLaRosaDeGuadalupe (bichos):
  from random import randint
  bichoelegido=randint(0,3)
  bichos[bichoelegido]+=10
def main():
  imprimirtia="""
abuelita tomada de https://textart.sh/topic/great-grandmother
 
                              ▓▓▓▓▓▓▓▓▓▓▓▓██                          
                        ▓▓▓▓▓▓░░░░░░░░░░░░░░▓▓▓▓▓▓                    
                    ▓▓▓▓░░░░      ░░░░    ░░░░░░░░▓▓▒▒                
                  ▓▓▓▓░░  ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░  ░░▓▓▓▓              
                  ▓▓▒▒░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░  ▒▒▓▓              
                ▒▒▒▒▒▒░░▓▓▒▒░░░░░░░░░░░░░░░░░░▓▓▓▓░░  ▒▒▒▒            
              ▓▓▒▒▒▒▒▒▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒░░░░▒▒▒▒          
              ▓▓▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░    ▓▓▓▓▒▒░░░░▓▓          
              ▓▓▒▒▒▒▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒░░▓▓          
              ▓▓▒▒▒▒▓▓▓▓░░▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒░░▓▓▓▓▒▒▒▒▓▓          
              ▓▓▒▒▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒▓▓          
                ▓▓▒▒▓▓░░▓▓████▓▓▓▓░░░░░░▓▓▓▓██▓▓▓▓░░▓▓▒▒▓▓            
              ▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒  ▓▓▓▓▓▓▓▓▓▓  ██  ▓▓▓▓▓▓▓▓▓▓▓▓          
              ▓▓░░░░▓▓░░▓▓      ▓▓░░░░░░██      ▓▓░░▓▓░░░░▓▓          
              ▓▓░░░░▓▓░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓██▓▓░░▓▓░░░░▓▓          
              ▓▓▓▓░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▓▓▓▓          
            ▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░▓▓▓▓              
            ▓▓▒▒▒▒▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓                
          ▓▓░░░░▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒              
          ▓▓░░▒▒▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓██▒▒          
          ▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░░░  ░░░░▓▓▓▓▒▒▒▒▒▒▒▒░░        
          ▓▓░░░░░░░░▒▒▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▒▒░░░░░░░░██      
        ▓▓░░░░░░  ░░░░▒▒▓▓▓▓▓▓░░░░░░░░░░░░░░▓▓▓▓▓▓▒▒░░░░░░░░░░░░██    
      ▓▓░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░  ░░░░░░░░██  
    ▓▓░░░░░░░░░░░░░░░░░░▒▒▓▓░░░░░░░░░░░░░░░░░░▓▓▒▒░░░░  ░░░░░░░░░░░░██
     _      _                                                            
  __| | ___| | ___    __ _    ___  ___  ___     ___ ___  _ __ ___   ___  
 / _` |/ _ \ |/ _ \  / _` |  / _ \/ __|/ _ \   / __/ _ \| '_ ` _ \ / _ \ 
| (_| |  __/ |  __/ | (_| | |  __/\__ \ (_) | | (_| (_) | | | | | | (_) |
 \__,_|\___|_|\___|  \__,_|  \___||___/\___/   \___\___/|_| |_| |_|\___/ 
                                          _                             
                                         /_/     _      
 ___ _   _    _ __ ___   __ _ _ __ ___   __ _   | | ___ 
/ __| | | |  | '_ ` _ \ / _` | '_ ` _ \ / _` |  | |/ _ \\
\__ \ |_| |  | | | | | | (_| | | | | | | (_| |  | |  __/
|___/\__,_|  |_| |_| |_|\__,_|_| |_| |_|\__,_|  |_|\___|
 
     _       _                               _           _                   
  __| | __ _| |__   __ _    __ _   _   _ ___| |_ ___  __| |   ___ ___  _ __  
 / _` |/ _` | '_ \ / _` |  / _` | | | | / __| __/ _ \/ _` |  / __/ _ \| '_ \ 
| (_| | (_| | |_) | (_| | | (_| | | |_| \__ \ ||  __/ (_| | | (_| (_) | | | |
 \__,_|\__,_|_.__/ \__,_|  \__,_|  \__,_|___/\__\___|\__,_|  \___\___/|_| |_|
 
 _              _                      _       
| | __ _    ___| |__   __ _ _ __   ___| | __ _ 
| |/ _` |  / __| '_ \ / _` | '_ \ / __| |/ _` |
| | (_| | | (__| | | | (_| | | | | (__| | (_| |
|_|\__,_|  \___|_| |_|\__,_|_| |_|\___|_|\__,_|
"""
  bichos=[]
  for i in range(4):
    bicho=int(input("Ingrese la vida del Bicho:"+str(i)+"\n"))
    bichos.append(bicho)
  while(True):
    menu(bichos)
    if (comprobarVida(bichos)):
     break
    accion = int(input("que opcion vas a escojer?:\n"))
    if(accion == 1):
      disparar(bichos)  
    if(accion == 2):
      pesticidas(bichos)
    if(accion == 3):
      vientoDeLaRosaDeGuadalupe (bichos)
    if(accion == 4):
      lluviaAcida(bichos)
    if(accion == 5):
      print(imprimirtia)
    if(accion == 0):
      break 
main()