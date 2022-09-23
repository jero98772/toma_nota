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
token::validtag(string charcter ,string letters,string nums,string simbols){
		if(letters.find(charcter)){
			ttag="l";
		}
		if(simbols.find(charcter)){
			ttag="s";
		}
		if(nums.find(exprecion[i])){
			ttag="n";
		}
}
token::identificartoken(){
	this->exprecion;
	string nums="1234567890";
	string letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
	string simbols="+-*/().";
	vector<string> tokens;
	char ttag="";
	char ttag2="";
	ttag=validtag(exprecion[0],letters,nums,simbols);
	ttag2=ttag;
	for(int i=1;i<exprecion.length();i++){
		ttag=validtag(exprecion[i],letters,nums,simbols);
		string t=t+exprecion[i];
		if(ttag!=ttag2){
			tokens.push_back(t);
		}
		ttag2=ttag;
	}
}

