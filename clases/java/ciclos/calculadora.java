import java.ulit.Scanner
public class calculadora{
	public static void main(String[] args){
		String opcion; 
		boolean continuar = true;
		Scanner input = new Scanner(System.in);
		while(continuar){
			System.out.println("escoja una de las siguintes opciones:\n\tsuma\t sume 2 numeros");
			opcion = input.nextString();
			System.out.println("ingrese el nuemro 1");				
			int num1 = input.nextInt();
			System.out.println("ingrese el nuemro 1");				
			int num2 = input.nextInt();
			switch(opcion){
				case "suma":
					System.out.println(num1+num2)
					break
				case "resta":
					break
				case "multiplicacion":
			
			} 
		}
	}
}