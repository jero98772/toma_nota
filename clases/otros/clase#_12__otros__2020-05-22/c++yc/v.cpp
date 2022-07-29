#include <bits/stdc++.h>
using namespace std;
void printmatvec(vector<vector<int>> &m,int size){
	for(int i=0;i<size;i++){
		for(int ii=0;ii<size;ii++){
			cout<<m[i][ii]<<" ";
		}
		cout<<endl<<endl;
	}
}
void printarr(int **m,int size){
	for(int i=0;i<size;i++){
		for(int ii=0;ii<size;ii++){
			cout<<m[i][ii]<<" ";
		}
		cout<<endl<<endl;
	}
}

int main(){
	int size;cin>>size;
	int arr[size][size];
	
	vector<vector<int>> matrix(size,vector<int>(size,88));
	printmatvec(matrix,size);
	//dont work//printarr(arr,size);
}
