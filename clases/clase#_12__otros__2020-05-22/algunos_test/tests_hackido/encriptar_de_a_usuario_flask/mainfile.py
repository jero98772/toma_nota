#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
encriptar_de_a_usuario_flask - 2020 - por jero98772
encriptar_de_a_usuario_flask - 2020 - by jero98772
"""
from flask import Flask, render_template, request, flash, redirect ,session
from Crypto.Cipher import AES
from Crypto import Random
import sqlite3
from hashlib import sha256
import random as rnd
app = Flask(__name__)
def enPassowrd(password):
	hashPassowrd = str(sha256(password.encode('utf-8')).hexdigest())
	return hashPassowrd
password = enPassowrd("sha.256")
slicepassword = slice(0,len(password),4)
print(len(password),"largo sha256")
print(password,"el sha256 /sha256 dividido 2",password[slicepassword])
print("hash de sha.256",app.secret_key,"el otro es", password )
realpass = password[slicepassword]
app.secret_key =  realpass
app.config['SECRET_KEY']
def encriptar(mensaje,key):
	mensaje = str(mensaje)
	key = str(key)
	print(key,"logitud",len(key))
	iv = Random.new().read(AES.block_size)
	cif = AES.new(key, AES.MODE_CFB,iv)
	mensaje = iv + cif.encrypt(mensaje)
	return mensaje
def desencriptar(mensaje,key):
	mensaje = str(mensaje)
	key = str(key)
	iv = Random.new().read(AES.block_size)
	dec = AES.new(key, AES.MODE_CFB,iv)
	mensaje = iv + dec.decrypt(mensaje)
	return mensaje
def busquedaespdb(data,sebusca):
	for i in data:
		print(i)
	key = app.secret_key
	sebusca = encriptar(sebusca,key)
	for datos in data:
		print(datos[4])
		if sebusca == datos[i]:
			return str(desencriptar(datos[4],key))
def busquedageneral(data):
	key = app.secret_key
	todosmsg = ""
	for i in data:
		print(i[0])
		todosmsg += str(desencriptar(i[0],key))
	return todosmsg
@app.route("/encriptar",methods=['GET','POST'])
def encriptarweb():
	connecting = sqlite3.connect("db_test")
	cursor = connecting.cursor()
	if request.method == 'POST':
		secreto = str(request.form["secreto"])
		key = app.secret_key#str(request.form["key"])
		#= enPassowrd(key)
		secreto = encriptar(secreto,key)
		cursor.execute("INSERT INTO test(data, pass) VALUES(?,?)",(secreto,"0"))#key)
		cursor.connection.commit()
	return render_template("encriptar.html")
@app.route("/desencriptar",methods=['GET','POST'])
def desencriptarweb():
	connecting = sqlite3.connect("db_test")
	cursor = connecting.cursor()
	#if request.method == 'POST':
	cursor.execute("SELECT data FROM test")
	datos = cursor.fetchall()
	print(datos)
	mensajedec = busquedageneral(datos)#hola socio ...
	return render_template("desencriptar.html",msgdec = mensajedec)
if __name__=='__main__':
	app.run(debug=True,host="0.0.0.0")
