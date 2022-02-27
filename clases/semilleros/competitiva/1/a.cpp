#include <bits/stdc++.h>
using namespace std;

int main(){
  int amountHumans,humanChoise;
  string dificult;
  cin >> amountHumans;
  for(int i=0;i<amountHumans;i++){
    cin>>humanChoise;
    if(humanChoise==0){
      dificult="EASY";
    }else{
      cout<<"HARD";
      break;
    }
    }
    if(humanChoise==0){
      cout<<dificult;
    }
  return 0;
}