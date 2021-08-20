import java.util.Scanner;
public class ContIncrDecr{
	public static void main(String[] args){
		double num = 0.0;
		int contador = 0;
		double mayor = 0;
		String movimientos="";
		Scanner input = new Scanner(System.in);
		do{
			num = input.nextDouble();
			if (num < mayor){
				contador=contador-1;
				movimientos = movimientos + "-1\n";
				//System.out.println("-1");
			}else{
				mayor = num;
				contador=contador+1; 
				//System.out.println("+1");
				movimientos = movimientos + "+1\n";
			}
		}while(num=0);
	System.out.println(contador);
	}
}