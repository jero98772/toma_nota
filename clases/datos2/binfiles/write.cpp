#include<iostream>
#include<fstream>
using namespace std;
int main(){
   ofstream wf("compress.bin", ios::out | ios::binary);
   if(!wf) {
      cout << "Cannot open file!" << endl;
   }else{
   	int p=192168;
   	wf.write((char *)&p, sizeof(p));
   }
   return 1;
}