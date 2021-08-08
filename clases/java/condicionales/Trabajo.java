import java.util.Scanner;
public class Trabajo{//
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("introdusca el dia:");
        int dia = input.nextInt();
        System.out.println("introdusca su salario:");
        double salario = input.nextDouble();
        switch(dia){
        case 1:
            salario = salario*1.455;
            break;
        case 2,3:
            break;
        case 4:
            salario = salario*1.1;
            break;
        case 5:
            salario = salario*1.295;
            break;
        case 6,7:
            salario = salario*1.75;
            break;
        }
        System.out.println("su salario es :");
        System.out.println(salario);
	}
}
