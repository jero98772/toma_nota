#ifndef automata_h
#define automata_h
#include <string>
class token{
	public:
		token(){};
		token(string exp){};
		~token(){}
		void identificartoken(){}
	private:
		char validtag(char c1,char c2){}
		string exprecion;
};
#endif