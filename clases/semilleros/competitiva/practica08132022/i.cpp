#include <bits/stdc++.h>
using namespace std;
int main(){
	int a,b,c,sum,m,ans;
	cin>>a>>b>>c;
	sum=a+b+c;
	m=sum/500;
	ans=sum-m*100;
	cout<<ans;
}