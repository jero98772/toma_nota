#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;
void tokenize(string const &str, const char* space,vector<string> &out){
    char *t = strtok(const_cast<char*>(str.c_str()), space);
    while (t != nullptr){
        out.push_back(string(t));
        t = strtok(nullptr, space);
    }
}
int verbo(vector<string> &tokens, string nombreArchivo){
    string linea;
    int validaciones=0;
    int pos;
        for(int i = 0; i < tokens.size(); i++){
        ifstream archivo;
        archivo.open(nombreArchivo,ios::in);
            if(archivo.is_open()){
                do{
                    archivo>>linea;
                    if(tokens[i]==linea){
                        validaciones++;
                        pos=i;
                    }
                    if(validaciones>=2){
                        cout<<"error"<<endl;
                        return -1;
                    }
                
            }while(!archivo.fail());
        }
        else{
            cout<<"error archivo no valido: "<<nombreArchivo<<endl;        }
        archivo.close();
    }
    
    if(validaciones==1){
        return pos;
    }
    if(validaciones==0){
        return -1;
    }
}
int sustantivos(vector<string> &tokens, string nombreArchivo,int pos){
    ifstream archivo;
    archivo.open(nombreArchivo,ios::in);
    string linea;
    int validaciones=0;

    for(int i = 0; i< pos; i++){
    if(archivo.is_open()){
        do{
            archivo>>linea;            
            if(tokens[i]==linea){
                validaciones=1;
				cout<<"Oracion valida\n"<<endl;
                break;
            }
        }while(!archivo.eof());
    }else{
        cout<<"error archivo no valido: "<<nombreArchivo<<endl;
        cout<<"revise que sus verbos o sustantivos esten en el archivo"<<endl;
    }
    }
    return validaciones;
}
int main(){
	string txt;
	getline(cin,txt);
	vector<string> out;
	tokenize(txt, " ", out);
	int pos=verbo(out,"verbos.txt");
	if (pos==-1){
		cout<<"la oracion no es valida"<<endl;
	}else{
		int esValido=sustantivos(out,"sustantivos.txt",pos);
		cout<<pos<<endl<<esValido<<endl;

	}
	return 0;
}