#include <bits/stdc++.h>
using namespace std;
int main(){
	//http://acm.hit.edu.cn/problemset/ 33
  int test,q,nq;
  cin>>test;
  string url; 
  for (int i=0;i<test;i++){
  	cin>>q>>nq;
  	int nums[q];

  	for(int ii=0;ii<q;ii++){
  		cin>>url;
        string urlnum=url.substr(33,url.length());
  		nums[ii]=stoi(urlnum);
  	}
  	int n=sizeof(nums)/sizeof(nums[0]);
  	sort(nums,nums+n);

  	for(int iii=0;iii<nq;iii++){
  		cout<<nums[iii]<<" ";
  	}
    cout<<endl;
  }
}