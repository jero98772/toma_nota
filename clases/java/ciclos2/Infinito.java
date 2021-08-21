import java.util.Scanner;
public class Infinito{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		boolean alert = true;
		int multiplicacion;
		do{
		int num = input.nextInt();
		if (num == 0){
			alert = false;
			break;
		}else{
			multiplicacion = num*3;
			System.out.println(multiplicacion);
		} 
		System.out.println();
		}while (alert);
	}
}