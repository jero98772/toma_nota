import java.util.Scanner;
public class PrincipalCalculadoraSimple{
    public static void main(String[] args){
        CalculadoraSimple cacl = new CalculadoraSimple();
        Scanner input = new Scanner(System.in);
        System.out.println("ingrse un numero entero");
        int num1 = input.nextInt();
        System.out.println("ingrse otro numero entero");
        int num2 = input.nextInt();
        int suma =  CalculadoraSimple.sumar(num1,num2);
        int resta = CalculadoraSimple.restar(num1,num2);
        System.out.println("el resultado es:");
        System.out.println("suma: "+num1+"+"+num2+"=");
        System.out.println(suma);
        System.out.println("suma: "+num1+"+"+num2+"=");
        System.out.println(resta);
    }
}
