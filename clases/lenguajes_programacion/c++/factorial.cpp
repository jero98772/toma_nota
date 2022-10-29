#include <iostream>
using namespace std;
int dp[100000];
int factorial(int n){
	if(dp[n]!=0){
		return dp[n];
	}
	if(n==1){
		return 1;
	}else{
		int ans=factorial(n-1)*n;
		dp[n]=ans;
		return ans;
	}	
}

int main(){
	int n;cin>>n;
	cout<<factorial(n);
}