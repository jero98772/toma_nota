#include "hola.h"
#include <stdlib.h>
#include <string>
#include <iostream>
using namespace std;
hola::hola(string txt){
	this->txt=txt;
}

void hola::saluda(){
	cout<<"Hola "<<this->txt<<endl;
}