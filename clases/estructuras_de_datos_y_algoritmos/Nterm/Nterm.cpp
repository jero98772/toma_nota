#include <iostream>
#include <string>
using namespace std;
int nterm(int n,int a,int b,int c){

}
int main(){
  int n;
  int pos1,pos2;
  string abc;
  cout<<"Ingrese 3 numeros de una sucession divididos por ,\n";
  cin>>abc;
  cout<<"Ingrese un numero x de la succesion:\n";
  cin>>n;
  char *strparts;
  pos1=abc.find(" ");
  pos2=abc.find(" ");
  strparts = strtok(abc, ","); 
  nterm(n)
  return 0;
}
