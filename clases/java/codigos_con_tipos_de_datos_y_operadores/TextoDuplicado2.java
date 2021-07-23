import java.util.Scanner;
public class TextoDuplicado {
  public static void main(String[] args) {
	System.out.println("ingrse una palabra para repetir 2 veces");
	Scanner ownInput = new Scanner(System.in);  
	String msg = ownInput.nextLine();	
	System.out.println(msg+msg);
  }
}