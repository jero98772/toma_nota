import java.util.Scanner;
public class Mesada{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		boolean alert = true;
		String name = input.next(); 
		while(alert){
			int money = input.nextInt();
			if (money>500){
				System.out.println(name+" eres mi angel");
				break;
			}else{
				System.out.println(name+" me decepcionas");
			}
		}
	}
}