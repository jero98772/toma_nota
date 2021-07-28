import java.util.Scanner;
public class hipotenusa {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("ingrese 2 numeros para calcular la hipotenusa");
        System.out.println("ingrese un numero a");
        float a = input.nextFloat();
        System.out.println("ingrese un numero b");
        float b = input.nextFloat();
        float hipotenusa = pow(pow(a,2)+pow(b,2),1/2)

    }
}
