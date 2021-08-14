import java.util.Scanner;
public class calculadora{
	public static void main(String[] args){
		String opcion; 
		int num1,num2;
		boolean continuar = true;
		Scanner input = new Scanner(System.in);
		while(continuar){
			System.out.println("escoja una de las siguintes opciones:\n\tsuma\t sume 2 numeros\n\tresta\t reste 2 numeros\n\tcuadrado\tsace el cuadrado de un numero\n\tsalir\t chao pescao");
			opcion = input.next();
			switch(opcion){
				case "suma":
					System.out.println("ingrese un numero");				
					num1 = input.nextInt();
					System.out.println("ingrese otro numero");				
					num2 = input.nextInt();
					System.out.println(num1+num2);
					break;
				case "resta":
					System.out.println("ingrese un numero");				
					num1 = input.nextInt();
					System.out.println("ingrese otro numero");				
					num2 = input.nextInt();
					System.out.println(num1-num2);
					break;
				case "cuadrado":
					System.out.println("ingrese un numero");				
					num1 = input.nextInt();
					System.out.println(num1*num1);
					break;
				case "salir":
					System.out.println("chao 🐟️");
					break;			
			} 
		}
	}
}