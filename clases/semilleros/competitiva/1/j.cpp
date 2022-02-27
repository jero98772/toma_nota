#include <bits/stdc++.h>
using namespace std;
int main(){
  int deckCards,card;
  cin>>deckCards;
  vector<int>vec(deckCards)
  for(int i=0;i<deckCards;i++){
    cin>>card;
    vec.push_back(card);
  }
  return 0;
}