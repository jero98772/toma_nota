import java.util.Scanner;
public class Word{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		String pal = input.nextLine();
		String palabra = pal.toLowerCase();
		System.out.println(palabra.length());
		System.out.println(palabra.indexOf("a"));
	}
}