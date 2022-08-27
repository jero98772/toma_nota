#include <bits/stdc++.h>
using namespace std;
int main(){
	int in,dis;
	int n=5;
	int mat[n][n];
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin>>in;
			if(in==1){
				//dis=abs(i-3)+abs(j-3);
				cout<<abs(i-2)+abs(j-2)<<endl;
				break;
                //cout<< abs(i-3)+abs(j-3)<<endl;
			}				
		}
	}
}