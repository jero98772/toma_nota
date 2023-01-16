#ifndef _HOLA
#define _HOLA
#include <stdlib.h>
#include <string>
using namespace std;
class hola{
	public:
		hola(string txt);
		void saluda();
	private:
		string txt;
};
#endif