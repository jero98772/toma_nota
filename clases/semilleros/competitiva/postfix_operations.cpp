#include <bits/stdc++.h>
using namespace std;
void solve(){
	stack<int> nums;
	int chars;cin>>chars;
	char data;
	int num,ans;
	for(int i=0;i<chars;i++){
		cin>>data;
		if(data=='+' || data=='-' ||data=='*' ||data=='/'){
			if(data=='+'){
				ans=nums.top();
				nums.pop();
				ans=ans+nums.top();
				nums.pop();
				nums.push(ans);
			}
			if(data=='-'){
				ans=nums.top();
				nums.pop();
				ans=ans-nums.top();
				nums.pop();
				nums.push(ans);
			}
			if(data=='*'){
				ans=nums.top();
				nums.pop();
				ans=ans*nums.top();
				nums.pop();
				nums.push(ans);
			}
			if(data=='/'){
				ans=nums.top();
				nums.pop();
				ans=ans/nums.top();
				nums.pop();
				nums.push(ans);
			}
		}else{
			num=stoi(data);//error with int of more than 2 digitis
			nums.push(num);
		}
	cout<<nums.top()<<endl;
	}
cout<<nums.size()<<endl;
	
}
int main(){

	int t;cin>>t;
	for(int i=0;i<t;i++){
		solve();
	}
}
