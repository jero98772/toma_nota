#include<iostream>
#include<fstream>
using namespace std;
int main(){
	ifstream wf("compress.bin",ios::binary);
	int p;
   	wf.read((char *)&p, sizeof(p));   
   	wf.close();
	cout<<p;
	return 1;
}