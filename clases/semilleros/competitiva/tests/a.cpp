#include <bits/stdc++.h>
using namespace std;
int main(){
 int a,b,c,d,t,p;
 cin>>t;
 for(int i =0;i<t;i++){
	 cin>>a>>b>>c>>d;
 	 p=0;
	 if (a<b){p=p+1;}
	 if(a<c){p=p+1;}
	 if(a<d){p=p+1;}
 
 	cout<<p<<endl;
	}
}