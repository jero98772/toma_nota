#include<iostream>

using namespace std;

 

class A

{

public:

  A()  { cout << "Constructor A ejecutado" << endl; }

};

 

class B

{

public:

 B()  { cout << "Constructor B ejecutado" << endl; }

};

 

 

 

class C: public A, public B  // Note the order

{

public:

  C()  { cout << "Constructor C ejecutado" << endl; }

};

 

int main()

{

    C objC;

    return 0;
}