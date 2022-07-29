#include <bits/stdc++.h>
using namespace std;
int main(){
	int val;
	int count=0;
	int arr1[3];
	int arr2[3];
	for(int i=0;i<6;i++){
		cin>>val;
		if(i>3){
			arr2[i-3]=val;
		}
		else{	
			arr1[i]=val;
		}
	}
	//sort()
	for(int i=0;i<3;i++){
		for (int j = 0; j < 3; j++) {
				if (arr1[i] < arr2[j]) {
					count++;
					arr2[j]=-1;
					break;
				}
			}
		}
	cout<<count;
}