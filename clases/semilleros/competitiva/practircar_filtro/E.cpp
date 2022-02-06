#include <iostream>
#include <string>
using namespace std;
int main(){
	int n,a,mana,minMana;
	cin>>n;
	for(int i=0;i<n;i++){
	 cin>>a;
	 mana=mana+a;
	 if (a<0){
       minMana=mana;
      }
	}
	cout<<minMana<<endl;
}
