#include <iostream>
#include <thread>

using namespace std;

void threadFunction(int id){
	cout<<"Thread"<<id<<"is running"<<endl
}

int main(){
	thread t1(threadFunction,1);
	thread t2(threadFunction,2);

	t1.join();
	t2.join();

}