import java.util.Scanner;
public class PrincipalCalculadoraSimple{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        CalculadoraSimple cacl = new CalculadoraSimple();
        int num1 = input.nextInt();
        int num2 = input.nextInt();
        int suma =  cacl.sumar(num1,num2);
        int resta = cacl.restar(num1,num2);
        System.out.println(suma);
        System.out.println(resta);
    }
}
