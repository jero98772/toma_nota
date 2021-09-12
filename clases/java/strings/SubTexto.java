import java.util.Scanner;
public class SubTexto{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.println("ingrese un texto");
		String txt1 = input.nextLine();
		System.out.println("ingrese una posion inicial de su texto , un numero entero");		
		int pos1 = input.nextInt();
		System.out.println("ingrese una posion final de su texto , un numero entero");
		int pos2 = input.nextInt();
		System.out.println(txt1.substring(pos1,pos2));
	}
}