import java.util.Scanner;
public class practica{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.println("ingrese el tamaño de array|");
		int num = input.nextInt();
		int[] larry = new int[num];
		for(int i=0;i<num;i++){
			larry[i] = 5;
		}
		System.out.println(larry[2]);
	}
}