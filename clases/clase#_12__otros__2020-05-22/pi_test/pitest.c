#include <stdio.h>
#include <math.h>

int main() {
   float pi =  3.1415;
   long double	pipow;
   pipow = pow(pi,pow(pi,pow(pi,pow(pi,pi))));
   printf("pi pi pi pi pi = %Lf",pipow);
   return 0;
}