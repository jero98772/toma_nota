import java.util.Scanner;
public class WithoutString{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		String txt1 = input.nextLine();
		String txt2 = input.nextLine();
		System.out.println(txt1.replace(txt2,""));
	}
}