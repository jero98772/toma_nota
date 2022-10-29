#include <bits/stdc++.h> 

using namespace std; 
bool isPalindrome(int x) { 
	string num=to_string(x);
     	string n=num;
	reverse(n.begin(), n.end());
	//reverse(x);
	//int n2=stoi(n);
	//cout<<n<<endl<<num<<n.compare(num)<<endl;
     	if(n==num){

		return true;
	}
	else{ 
		return false;
	}
} 
 
int main() { 
    int n; 
    cin >>n;
    //cout<<isPalindrome(n)<<endl; 
    if(isPalindrome(n)) { 
        cout <<n<<" is a palindrome"; 
    } 
    else { 
        cout << n<<" is NOT a palindrome"; 
    } 
    return 0; 
}