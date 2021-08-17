import java.util.Scanner;
public class ContIncrDecr{
	public static void main(String[] args){
		double num = 0.0;
		int contador;
		int mayor;
		Scanner input = new Scanner(System.in);
		do{
			num = input.nextDouble();
			if (num < mayor){
				contador--
			System.out.println("-1");
			}else{
				mayor = num
				contador++ 
			System.out.println("+1");
			}
		}while(num==0);
	System.out.println(contador);
	}
}