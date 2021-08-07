import java.util.Scanner;
public class ParImpar{
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);
	int num = input.nextInt();
	if (num%2==0){
		System.out.println("es par");
	}else{
		System.out.println("es impar");
		}	
	}
}