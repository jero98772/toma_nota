#include <bits/stdc++.h>
using namespace std;
unsigned long int dp[100000];
unsigned long int catalan(unsigned int n){
	if(dp[n]!=0){
		return dp[n];	
	}else{
		if(n<=1){
			return 1;
			}
		else{
		unsigned long int res=0;
		for(int i=0;i<n;i++){
			res+=catalan(i)*catalan(n-i-1);
			//cout<<res;
		}
		dp[n]=res;
		return res;
		}
	}
}
int main(){
	int n;cin>>n;
	//for(int i=0;i<n;i++){dp[i]=-1;}	
	cout<<catalan(n+1);
}

