#include <stdio.h>

int main(){
	int entrada;
	char entradac[50];
	char strogen[100];
	printf("escribe algo \n");
	scanf("%i",&entrada);
	printf("\ntu entrada fue %i \n",entrada );
	printf("escribe algo \n");
	scanf("%s",entradac);
	printf("\ntu entrada fue %s \n",entradac );
	printf("escribe algo \n");
	gets(strogen);
	printf(" \ntu entrada fue %s \n",strogen );
	return 0;
}
