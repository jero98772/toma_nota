#include <iostream> 
//passed on sololearn code
using namespace std; 
 
int main() { 
    int ages[5]; 
    for (int i = 0; i < 5; ++i) { 
        cin >> ages[i]; 
    } 
    int min=ages[0];
    for(int i=1;i<5;i++){
       if (min>ages[i]){
           min=ages[i];
       }
     }
     float dec=50*(min/100.0);
     //cout<<dec<<endl;
     float val=50-dec;
     cout<<val<<endl;
    return 0; 
}
