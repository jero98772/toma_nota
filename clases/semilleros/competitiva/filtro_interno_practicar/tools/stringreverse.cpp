#include <bits/stdc++.h>
using namespace std;
int main(){
	string out="";
	string in;cin>>in;
	stack<string> st;
	for(int i=0;i<in.size();i++){
		st.push_back(in[i])
	}
	for(int i=0;i<in.size();i++){
		out=st.pop_back();
	}

}