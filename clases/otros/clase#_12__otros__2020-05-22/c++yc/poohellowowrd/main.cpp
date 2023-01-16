#include <stdlib.h>
#include "hola.h"
#include <iostream>

using namespace std;
int main(){
	string name;cin>>name;
	hola saludar=hola(name);
	saludar.saluda();
}