import java.util.Scanner;
public class invertir_numero {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Ingrese 2 numeros para multiplicarlos y sumarlos");
        System.out.println("Ingrese un numero entero");
        int num1 = input.nextInt();
        System.out.println("Ingrese otro numero entero");
        int num2 = input.nextInt();
        int multiplicacionResultante = num1*num2;
        int sumaResultante = num1+num2;
        System.out.println(multiplicacionResultante);
        System.out.println(sumaResultante);
    }
}

