#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
string cifer(string txt,int key, string alphabet){
  string enc="";
  for(int i=0;i<txt.size();i++){
    int pos=(alphabet.find(txt[i])+key)%alphabet.size();
    enc+=alphabet[pos];
  }
  return enc;
}
string decifer(string txt,int key, string alphabet){
  string enc="";
  for(int i=0;i<txt.size();i++){
    int pos=(alphabet.find(txt[i])-key)%alphabet.size();
    enc+=alphabet[pos];
  }
  return enc;
}
int equals(string s1,string s2,int size){
  int counter=0;
  for(int i=0;i<size;i++){
    if(s1[i]==s2[i]){
      counter+=1;
      cout<<counter<<endl<<s1[i]<<s2[i]<<endl;
    }
  }
  return counter;
}
int maxset(){}
int main(){
  string alphabet="abcdefghijklmnopqrstuvwxyz";
  string worddecf,wordcif,encript,decript;
  int wordsize;
  cin>>wordsize;
  cin>>wordcif;
  cin>>worddecf;
  set<int> ocurrences;
  for(int i=0;i<alphabet.size();i++){
    encript=cifer(worddecf,i,alphabet);
    decript=decifer(wordcif,i,alphabet);
    //cout<<encript<<endl;//<<decript<<endl;
    ocurrences.insert(equals(worddecf,decript,wordsize));
    ocurrences.insert(equals(wordcif,encript,wordsize));
    //swap
  }
  /*for(int i=0;i<alphabet.size();i++){
    encript=cifer(worddecf,i,alphabet);
    decript=decifer(wordcif,i,alphabet);
    cout<<encript<<endl<<decript<<endl;
    //swap
  }*/
  for(auto el=ocurrences.begin();el!=ocurrences.end();el++){
  cout<<*el<<endl;
  }
  int maxnum=*max(ocurrences.begin(),ocurrences.end());
  cout<<maxnum<<endl;
  return 0;
}
