#include <bits/stdc++.h>
using namespace std;
string solve(string data){
	stack<char> s;
	for(int i=0;i<data.length();i++){
		if(data[i]=='(' || data[i]=='[' || data[i]=='{'){
			s.push(data[i]);
		}else if(data[i]==')' || data[i]==']' || data[i]=='}'){
			if(s.empty()){
				return "NO";
				break;
			}else{
				if(data[i]==')'){
					if(s.top()=='('){
						s.pop();
					}else{
						return "NO";
					}
				}
				if(data[i]==']'){
					if(s.top()=='['){
						s.pop();
					}else{
						return "NO";
					}
				}
				if(data[i]=='}'){
					if(s.top()=='{'){
						s.pop();
					}else{
						return "NO";
					}
				}
			}
		}
	}
	if(s.empty()){//is balanced?
		return "YES";
	}else{
		return "NO";
	}
}
int main(){
	string data;cin>>data;	
	cout<<solve(data)<<endl;
}