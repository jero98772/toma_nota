# canuco (es para una tarea de la U )
# en desarrollo
        asciiart  de ejm98 y jero98772
                _____
               |A .  | _____
               | /.\ ||A ^  | _____
               |(_._)|| / \ ||A _  | _____
               |  |  || \ / || ( ) ||A_ _ |
               |____V||  .  ||(_'_)||( v )|
                      |____V||  |  || \ / |
                             |____V||  .  |
                                    |____V|
      un juego de memoria
        ____    _    _   _ _   _  ____   _____
       / ___|  / \  | \ | | | | |/ ___/ |  ^  |
      | |     / _ \ |  \| | | | | |     | / \ |
      | |___ / ___ \| |\  | |_| | |___  | \ / |
       \____/_/   \_\_| \_|\___/ \____\ |  V  |
                                         =====                                      
      cartas y numeros = concentracion
                _____
               |A .  | _____
               | /.\ ||A ^  | _____
               |(_._)|| / \ ||A _  | _____
               |  |  || \ / || ( ) ||A_ _ |
               |____V||  .  ||(_'_)||( v )|
                      |____V||  |  || \ / |
                             |____V||  .  |
                                    |____V|
# TODO list (aqui se pone las cosas que quedaron pendientes) o sueños alejados y no comprendidos por esta realidad
1- hacer que las parejas no salgan cada cantidadFichas/2 [preterminadamente es cada des fichas 10]

2- hacer que las fichas tengan un numero de referencia y con el que existan diferentes columnas y filas dependiendo de la cantiad de fichas selecionadas

3- introducir un manual de juego que pueda ver  el usuario en consola  antes de jugar o para aprender a jugar (mientras se llega a  escribir ,buscar --> y llege al codigo va a tener un aviso que dise "suponemos que usted sabe jugar canuco es como jugar un juego de memoria o concetrese etc... "

4- integrar un menu pricipal pal juego  

5- crear una forma para para que se pueda jugar mas de 2 personas o robots y que no dependa la cantiadad de personas la forma del codigo que lo pueda definir el usuario

puede ser con esta idea :se pueden hacer mas de 2 jugadores y los quequiera con un for ,eval con el indicie del for concatenarlo al codigo que esta en eval 

-- que no exista un limite para los jugadores  -->  no nos fue muy bien debido a que la eval() no aceptava muy bien la declaracion de variables dentro de un str

se podria llegar a el con propocionar la cantidad de fichas por jugadores (digamos 7 jugadores las fichas pueden ser 70)--> me gusta mas esta por si se quiere hacer el todo 6 seria mas compatible

o

por la mitad de cantidad de fichas  sea el numero permitido de jugadores --> esta puede ser  para el numero prederminado de fichas

sugerencia : se pueden hacer las 2 al mismo tiempo para controlar tanto lo predetrminado como las eleciones

6- que se puedan sacar parejas , trios , cuartetos de las fichas y que lo pueda definir el usuario

7- borrar la consola o limpiar la pantalla de la terminal cada ves que un jugador saca sus 2 cartas

### una de las librerias de generacion de numeros aleatorios fue desarrollada por jero98772                                

# algunas notas de desarrollo
#### D--°> un ciclo para identificar las fichas
se nesesita un ciclo para identificar las fichas que estan dentro un vector
#### D--°> otro ciclo para los turnos
para que se repita cuntas veces se ejecute el codigo hasta que se ecnutren todas las fichas
#### o / y
se puede optimisar  con un contador si se encuentran las fichas se quita o se rompe el programa mientras el codigo para  encontrar fichas esta dentro de una funcion

#### D--°> pueden existir mas fichas que turnos ?
si ,si se quiere dejar incompleto el juego 

#### D--°> pueden existir mas turnos que fichas ?

si ,si para que existan diferentes oportunidades de vulver a encontrar las fichas siempre que no vuelvan a exitir las oportunidades se acaben cuando se acaben las fichas

# algunas notas del juego
#### D--°> si el jugador encunetra una pareja el juego dice que tiene otro turno hasta que no encuentre una nueva pareja

#### D--°> hay que limpiar la consola para evitar que el juador se pueda devolver a ver sus momientos en el pasado y no usar el poder del recuerdo

#### no se puede comparar  la primera ficha con la segunda que estan en la misma pocion
puede funcionar elecion1 != elecion2 y/ and valorfichas[eleccion2] == valorfichas[eleccion2]
# correcciones y mejoras
#### cambiar y mejorar los idices de las cartas
se puede lograr sin alterar el bucle y poniendole un condicional
para que excluya el print(i el indice)
#### exluir el false si es el valor de la ficha que lo diga algo diferente
#### si saca parejas que repita
#### dar un fedback si saca parejas
#### dar puntaje para cada jugador
#### poner diferentes filas y columnas
#### poner para que salga el dibujo del ascii art de las cartas siendo diferente a 20