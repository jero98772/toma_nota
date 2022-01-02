#include <iostream>
using namespace std;
int fibo(int n){
     if(n<=1){
         return n;
     }
     else{
         return(fibo(n-1)+fibo(n-2));
     }
}
int main(){
    int n,fiboNum;
    cout<<"ingrese un numero para calcular fibonacci\n";
    cin>>n;
    fiboNum=fibo(n);
    cout<<"\n"<<fiboNum<<"\n";
    return 0;
}