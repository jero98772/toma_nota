#include <iostream>
#include <string>
#include <vector>
#include "automata.h"

token::token(){}
token::token(string exp){
	this->exprecion=exp;
}
token::~token(){
	exprecion.clear();
}
token::identificartoken(){
	this->exprecion;
	string nums="1234567890";
	string letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
	string simbols="+-*/().";
	vector<string> tokens;
	char ttag="":
	for(int i=0;i<exprecion.length();i++){
		string t=t+exprecion[i];
		if(letters.find(exprecion[i])){
			ttag="l";
		}
		if(simbols.find(exprecion[i])){
			ttag="s";
		}
		if(nums.find(exprecion[i])){
			ttag="n";
		}
		//cuando reconosca un token mandar un mensaje
	}
}

