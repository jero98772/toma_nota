import java.util.Scanner;
public class Multiplos5{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		int numero = input.nextInt();
		int acumulador = 0 ;
		while (numero>acumulador){
			acumulador = acumulador+5;
			System.out.println(acumulador);
		}
	}
}