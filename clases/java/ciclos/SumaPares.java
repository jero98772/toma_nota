import java.util.Scanner;
public class SumaPares{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("ingrse la cantidad de numeros a ingresar");
        int num = input.nextInt();
        int i = 0;
	int acumulador = 0;
        while(i<num){
		System.out.println("ingrse un numero:");
		int nuevoNumero = input.nextInt(); 
		if (nuevoNumero %2 == 0){
			acumulador = acumulador + nuevoNumero;
		}
		i = i + 1;
	}
	System.out.println("el resultado es :");
	System.out.println(acumulador);
    }
}
