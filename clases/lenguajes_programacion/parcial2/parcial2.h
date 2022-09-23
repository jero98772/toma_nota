#ifndef parcial2_h
#define parcial2_h
#include <ctime>
#include <cmath>
#include <math.h>
#include <string>
int aleatorio(int menor, int mayor);
double seno(int angulo);
class lanzamiento{
	public:
		lanzamiento();
		~lanzamiento();
		std::string toString();
		void sigLanzamiento(lanzamiento sig);
		*lanzamiento getSigLanzamiento();
		float distancia();
	private:
		int velocidad;
		int angulo;
		float distanciaVar;
		lanzamiento siguiente;

};


#endif
