#include <iostream>
using namespace std;
void f(int a){
  a = a + 1;
  cout << "En metodo: " << a << "\n";
}

int main(int argc, char *argv[]){
  int a = 5;
  f(a);
  cout << "En main: " << a << "\n";
}