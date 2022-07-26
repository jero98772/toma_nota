#include <bits/stdc++.h>
using namespace std;
int main(){
	int n;cin>>n;
	int board[n][n];
	if(n<4){
	 	cout<<n<<"n invalido";
	}else{
		//add defautl value for matrix, if you create matrix in main() or other function normal values will be random, but if you create out of function was fill with 0 
		for(int i=0;i<n;i++){
				for(int ii=0;ii<n;ii++){
					board[i][ii]
			}
		}
	}
}
//https://www.cs.buap.mx/~zacarias/FZF/nreinas3.pdf
//https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/