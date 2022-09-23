#include "parcial2.h"
#include <iostream>
#include <string>

using namespace std;

int aleatorio(int menor, int mayor)
{
	srand((unsigned) time(0));

	return(menor + (rand() % (mayor - menor)));
}

double seno(int angulo)
{
	return(sin((double)angulo * M_PI/180));	
}


lanzamiento::lanzamiento(){
	do{
		this-> velocidad=aleatorio(25, 55);
		this-> angulo=aleatorio(0, 85);
		this->distanciaVar=this->distancia();
	}while(this->distanciaVar<49 && this->distanciaVar>126);
}
lanzamiento::~lanzamiento(){
	this->distanciaVar=0;
	this->velocidad=0;
	this->angulo=0;
}
float lanzamiento::distancia(){
	float gravedad=9.81;
	float x=((this->velocidad^2)/gravedad)*seno(2*this->angulo);
	return x;
}
string lanzamiento::toString(){
	string txt="Siguiente lanzamiento\n---------------------\nVelocidad inicial: "+to_string(this->velocidad)+" m/s\nAngulo: "+to_string(this->angulo)+"\nDistancia: "+to_string(this->distanciaVar)+" mts\n---------------------";
	return txt;
}
void lanzamiento::sigLanzamiento(lanzamiento sig){
	this->siguiente=*sig;
}
lanzamiento *lanzamiento::getSigLanzamiento(){
	return this->siguiente;
}

int main(){

	int size=10;
	lanzamiento head=new lanzamiento();

	//generar lanzamientos
	lanzamiento tmp=head;
	for(int i=0;i<size;i++){
		lanzamiento* node= new lanzamiento();
		tmp.sigLanzamiento(node);
		tmp=node;
	}	

	//mostrar lanzamientos
	tmp=head;
	for(int i=0;i<size;i++){
		cout<<tmp.toString()<<endl;
		tmp=tmp.getSigLanzamiento();
	}
}