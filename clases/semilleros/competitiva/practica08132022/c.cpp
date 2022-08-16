#include <bits/stdc++.h>
using namespace std;
int main(){
	int t,n,m,ans;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>n>>m;
		n+=1;
		m+=1;
		ans=(((n*m)*(n+1))/2)%1000000007;
		cout<<ans<<endl;
	}
}