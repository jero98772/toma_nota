#include <iostream>
using namespace std;
int main(){
	int n,*dir;cin>>n;
	dir=&n;
	cout<<*dir<<endl;
	cout<<dir<<endl;
	cout<<n<<endl;
	cout<<&n<<endl;
}