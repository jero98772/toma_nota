#include <iostream>
//numero de 3 digitos alreves 
using namespace std;
int main(){
  int num;

  cout <<"introduce un numero de 3 cifras"<<endl;
  cin>>num;
  if(-1000<num<1000 && -99<num<99){
    int resultado;
    int proceso;
    int dig1 = num/100;
    float dig2 = ((num/10)%10)*10;
    float dig3 = (num%10)*100;
    resultado = dig3+dig2+dig1;
      cout<<"el resulatdo es: "<<resultado <<endl;
  }
  else{
    cout << "numero no valido"<<endl;
  }
  return 0;
}
