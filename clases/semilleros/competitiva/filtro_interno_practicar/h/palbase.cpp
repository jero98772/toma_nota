#include <bits/stdc++.h>
using namespace std;
int main(){
	string n1, n2,nn;
	int n;cin>>n;
	n1=to_string(n-1);
	n2=n1;
	reverse(n2.begin(), n2.end());
	//cout<<n2.size();
	nn=n1+n2.substr(1);
	cout<<nn<<endl;
}
