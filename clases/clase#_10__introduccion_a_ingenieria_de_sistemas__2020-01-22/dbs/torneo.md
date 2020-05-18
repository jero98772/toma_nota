# ejercios
este es ::::Crear una base de datos que controle los jugadores de futbol del torneo nacional de Colombia. Crear dos tablas:
•	EQUIPOS (cod_equipo (pk), nombre, ciudad, cantidad de torneos ganados, tipo de torneo (internacional, nacional, departamental).

	CREATE TABLE equipos (cod_equipo  TEXT PRIMARY KEY, nombre TEXT, ciudad TEXT, torneos_ganados INTEGER, tipotorneo TEXT)
•	JUGADORES (dni (pk), nombre, apellido, posición, estatura, equipo_actual, fecha_de_nacimiento, cod_equipo(fk))

	CREATE TABLE jugadores (dni PRIMARY KEY, nombre TEXT, apellido TEXT, posicion TEXT, estatura REAL, equipo_actual TEXT, fecha_de_nacimiento TEXT,cod_equipo TEXT REFERENCES equipos(cod_equipo))

•	GOLES ANOTADOS (cod, equipo_gol, equipo_recibio, fecha, dni_jugador , dni_jugador (fk))
	
	CREATE TABLE goles (cod , equipo_gol TEXT, equipo_recibio TEXT, fecha TEXT, dni_jugador TEXT REFERENCES jugadores(dni) ,cantidad INTEGER)

1.	Crear las relaciones entre las tablas [DONE] 
	poniendio references table(elemento que nesesito)
2.	Goleador  (mostrar todos los campos)
	
		SELECT * FROM goles

3.	Buscar los goles anotados en una fecha especifica

		SELECT * FROM goles WHERE fecha = "ayer"

4.	Promedio goles por jugador
		
		SELECT avg((SELECT count(dni_jugador) FROM goles WHERE dni_jugador = "104")) FROM goles


5.	Encontrar el jugador que más goles anoto en un partido
		
		SELECT max(cantidad) FROM goles

6.	Determinar el equipo que más goles recibió
		
		SELECT equipo_recibio FROM goles WHERE cantidad=(SELECT max(cantidad) FROM goles)
7.	Equipo que más goles anoto

		SELECT equipo_gol FROM goles WHERE cantidad=(SELECT max(cantidad) FROM goles)
8.	Los equipos a los cuales “Ananías Giraldo” les metió gol
		
		SELECT equipo_recibio FROM goles WHERE dni_jugador = "104"

9.	Arqueros que han metido goles

		SELECT * FROM goles WHERE dni_jugador  = (SELECT dni FROM jugadores WHERE posicion = "arquero")

10.	El defensa que más goles anoto

		SELECT max(cantidad) FROM goles WHERE dni_jugador  = (SELECT dni FROM jugadores WHERE posicion = "defensa")

11.	Jugadores que nunca han metido goles

		SELECT cantidad FROM goles WHERE cantidad  < 0
12.	El jugador más alto que ha anotado gol (o goles)
	
		SELECT dni_jugador FROM goles WHERE dni_jugador  = (SELECT dni FROM jugadores WHERE  estatura = (SELECT max(estatura) FROM jugadores ))

13.	El promedio de goles anotados por un jugador
		
		SELECT avg(cantidad) FROM goles

14.	La suma total de goles anotados a Nacional
		
		SELECT sum(cantidad) FROM goles WHERE equipo_recibio = "nacional"

15.	El promedio de goles anotados por Medellín
		
		SELECT avg(cantidad) FROM goles WHERE equipo_gol= "medellin"

16.	Equipo con más trofeos
		
		SELECT max(torneos_ganados) FROM equipos
# procedimiento

####crear tablas
	CREATE TABLE equipos (cod_equipo  TEXT PRIMARY KEY, nombre TEXT, ciudad TEXT, torneos_ganados INTEGER, tipotorneo TEXT)
	CREATE TABLE jugadores (dni PRIMARY KEY, nombre TEXT, apellido TEXT, posicion TEXT, estatura REAL, equipo_actual TEXT, fecha_de_nacimiento datetime,cod_equipo TEXT REFERENCES equipos(cod_equipo))
	CREATE TABLE goles (cod , equipo_gol TEXT, equipo_recibio TEXT, fecha datetime, dni_jugador TEXT REFERENCES jugadores(dni) )
####ingresar datos
equipos
	
	INSERT INTO  equipos VALUES("10","los camellos","maya",8,"departamental")
	INSERT INTO  equipos VALUES("11","los bluedepsy","inca",-8,"internacional")
	INSERT INTO  equipos VALUES("12","los escorpion","azteca",-31415,"nacional")
	INSERT INTO  equipos VALUES("13","los cactus","atlantis",2781,"barrio")
	INSERT INTO  equipos VALUES("14","la arena","egipto",2781,"escolar")
	INSERT INTO  equipos VALUES("15","nacional","medellin",1,"departamental")
	INSERT INTO  equipos VALUES("16","nacional","medellin",0,"departamental")
jugadores
	
	INSERT INTO  jugadores VALUES("100","socrates","nikiforv","arquero",1.87,"maya","-1/1/400","10");
	INSERT INTO  jugadores VALUES("101","Ananías malvado","Giraldo","arquero",1.85,"inca","4/2/200","11");
	INSERT INTO  jugadores VALUES("102","Ananías clon","Giraldo","deleantero",1.85,"azteca","4/2/200","12");
	INSERT INTO  jugadores VALUES("103","Ananías real","Giraldo","recoje balones",1.85,"atlantis","4/20/1999","13");
	INSERT INTO  jugadores VALUES("104","Ananías","Giraldo","defensa",1.83,"egipto","4/20/2019","14");
	INSERT INTO  jugadores VALUES("107","haciendo","tarea","delantero",1.86,"medellin","4/20/2018","16");
	INSERT INTO  jugadores VALUES("106","armando","maqueta","delantero",1.86,"nacional","4/20/2018","15");
goles 
	
	INSERT INTO goles VALUES (1000, "maya","inca","ayer","100",1);
	INSERT INTO goles VALUES (1001, "inca","maya","ayer","101",1);
	INSERT INTO goles VALUES (1002, "maya","inca","ayer","100",1);
	INSERT INTO goles VALUES (1003, "maya","inca","ayer","100",1);
	INSERT INTO goles VALUES (1004, "maya","inca","ayer","100",1);
	INSERT INTO goles VALUES (1005, "egipto","inca","hoy","104",1);
	INSERT INTO goles VALUES (1006, "inca","egipto","hoy","101",1);
	INSERT INTO goles VALUES (1007, "egipto","inca","hoy","104",1);
	INSERT INTO goles VALUES (1008, "egipto","inca","hoy","104",1);
	INSERT INTO goles VALUES (1009, "egipto","inca","hoy","104",1);
	INSERT INTO goles VALUES (1010, "azteca","inca","mañana","102",1);
	INSERT INTO goles VALUES (1011, "azteca","inca","mañana","102",1);
	INSERT INTO goles VALUES (1012, "azteca","inca","mañana","102",1);
	INSERT INTO goles VALUES (1013, "azteca","inca","mañana","102",1);
	INSERT INTO goles VALUES (1014, "azteca","inca","mañana","102",1);
	INSERT INTO goles VALUES (1015, "azteca","inca","mañana","102",1);
	INSERT INTO goles VALUES (1016, "azteca","inca","mañana","102",1);
	INSERT INTO goles VALUES (1017, "medellin","inca","mañana","107",1);
	INSERT INTO goles VALUES (1018, "medellin","inca","mañana","107",1);
	INSERT INTO goles VALUES (1019, "nacional","inca","mañana","106",1);
	INSERT INTO goles VALUES (1020, "inca","nacional","ayer","106",1);



####ver datos
	SELECT * FROM equipos
	SELECT * FROM jugadores 

#### si se nesesita cambiar algunas cosas
	DROP TABLE equipos
	DROP TABLE jugadores
o

	UPDATE <tabla> set <cambios> where id = id
	DELETE FROM <tabla> WHERE  id = id 	

# algunas notas 
crear una base de datos para torneos de futbol
crear una tabla para los jugadores,cod equipo nombre ciudad ,cantidad de torneos gandos
tipo torneo(nacional,internacional,departamental)
jugador (dni(primari key),nombre,apeellido,posion,equipo_actual,fecha_nacimiento)
goles (cod (primari key),equipo_gol,equipo_recibido,fecha,dni_jugador)
equipo(cod equipo)
equipos->jugadores-> goles
1crear relaciones entre las tablas
2goleador (todos los campos) select * from  goles
3buscar los goles
los equipos a los que ananias les metio gol


