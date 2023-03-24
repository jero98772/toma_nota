hacer 2 bases de datos relacionadas de una clinica de 

pacientes

tabla 

	CREATE TABLE paciente (dni TEXT PRIMARY KEY,nombre TEXT NOT NULL ,apellido TEXT NOT NULL , email TEXT, estatura REAL,tiposangre TEXT NOT NULL);
	INSERT into paciente VALUES ("101","sappote","gonsales","perdio@gmail.cc",150,"o-")
	INSERT into paciente VALUES ("101","sapo","peres","perdio@hotmail.cc",120,"o+")

	SELECT * FROM paciente
medicos

	CREATE TABLE medico (dni TEXT PRIMARY KEY,nombre TEXT NOT NULL ,apellido TEXT NOT NULL , conatacto TEXT, campo_ocupado TEXT, revisa_A  TEXT REFERENCES paciente(dni));
	INSERT into medico VALUES ("104","sabo","alto","404@hotmail.cc","medico_general","100")
	
	SELECT * FROM medico
por si algo
	DROP TABLE medico 
citas
