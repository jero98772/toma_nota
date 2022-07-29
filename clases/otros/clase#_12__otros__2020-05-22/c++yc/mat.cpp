#include <bits/stdc++.h>
using namespace std;
void printmat(int m&,int n){
	for(int i=0;i<n;i++){
		for(int ii=0;ii<n;ii++){
			cout<<m[i][ii];
		}
	cout<<endl;
	}
}
int main(){
	int size;
	cin>>size;
	vector<vector<int>> mat(size,(size,0));
	for(int i=0;i<size;i++){
		for(int ii=0;ii<size;ii++){
			mat[i][ii]=i*ii;
		}
	}
	printmat(mat,size);
}