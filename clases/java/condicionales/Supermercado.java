import java.util.Scanner;
public class Supermercado{
	public static void main(String[] args){
		int basePoints = 5;
		System.out.println("ingrese el tipo de producto");
		System.out.println("tipo (1), le dan 5 puntos");	
		System.out.println("tipo (2), le dan 10 puntos");
		System.out.println("tipo (3), le dan 15 puntos");
		System.out.println("...");
		Scanner input = new Scanner(System.in);
		int typeOfProduct = input.nextInt();
		System.out.println("ingrese la cantidad de productos");
		int amountOfProducts = input.nextInt();
		int earnedPoints = amountOfProducts*(typeOfProduct*basePoints);
		System.out.println("la cantidad de puntos obtenidos con su compra son:");
		System.out.println(earnedPoints);
		
	}
}