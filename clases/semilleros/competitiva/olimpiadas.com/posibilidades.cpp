#include <bits/stdc++.h>
using namespace std;
void gencombinations(int n,string s,int i,string lists){
	if(i==n){
		cout<<s<<endl;
	}else{
		for(int j=0;j<lists.size();j++){
			gencombinations(n+1,s+lists[j],i,lists);
		}
	}
}
int main(){
	gencombinations(0,"",10,"abcdefghijklmnñopqrstuvwxyz");
}