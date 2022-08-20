#include <bits/stdc++.h>
using namespace std;

int main(){
 					srand(time(NULL));
          int num1,num2,num3,num4,total,input,rndnum;
          //num1=rand()%100+1
          //num2=rand()%100+1
          //num3=rand()%100+1
          int nums[3]={rand()%10+1,rand()%10+1,rand()%10+1};
          total=nums[0]+nums[1]+nums[2];
          rndnum=rand()%3;
          num4=nums[rndnum];
          nums[rndnum]=-1;
          bool alert1=false;
          bool alert2=false;
          bool alert3=false;
          int c=0;
          string txt="__+"+to_string(num4)+"+__="+to_string(total);
					cout<<txt;
					cout<<"input number for sum , -1 for exit"<<endl;
					do{
						cin>>input;
						if(input==rndnum || input>3 ){
							cout<<"chose other number"<<endl;
						}
						if(input==nums[0] && rndnum!=0 && !alert1){
							alert1=true;
							cout<<"your number is CORRECT"<<endl;
							c++;
						}
						if(input==nums[1] && rndnum!=1 && !alert2){
							alert2=true;
							cout<<"your number is CORRECT"<<endl;
							c++;
						}
						if(input==nums[2] && rndnum!=2 && !alert3){
							alert3=true;
							cout<<"your number is CORRECT"<<endl;
							c++;
						}if(c==2){
							cout<<"you win"<<endl;
						}
					}while(input!=-1);	
}