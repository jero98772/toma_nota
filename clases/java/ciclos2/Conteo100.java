import java.util.Scanner;
public class Conteo100{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		boolean alert = true;
		int numsOver100 = 0 ;
		while(alert){
			int num = input.nextInt();
			if (num>100){
				numsOver100++;
			}if(num == 0){
				System.out.println(numsOver100);
				break;
			}

		}
	}
}