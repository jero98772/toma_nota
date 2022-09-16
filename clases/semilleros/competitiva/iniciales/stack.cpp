#include <bits/stdc++.h>
using namespace std;
int solve(s){
	stack<char> st;
	for(int i=0;i<s.length();i++){
		if(s[i]=="("){
			st.push("(")
		}
		if(s[i]==")"){
			if(st.empty()){
				return 0;
			}else{
				st.pop();
			}
		}
	}
	if(st.empty()){
		return 1;
	}
}
int main(){
	string s;cin>>s;
	int a=solve(s);
	if (a==1){
		cout<<"YES"<<endl;
	}else{
		cout<<"NO"<<endl;
	}
}
