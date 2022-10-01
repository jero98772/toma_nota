#include <iostream>
using namespace std;

float n=0.5;
float *pn=&n;
int main(int argc, char const *argv[]){
	cout<<*pn<<endl;	
	return 0;
}