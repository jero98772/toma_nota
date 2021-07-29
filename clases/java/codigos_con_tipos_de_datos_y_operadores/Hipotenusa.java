//codigo libre
//licencia de Creative Commons Reconocimiento 4.0 Internacional
//por jero98772
import java.util.Scanner;
public class hipotenusa {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("ingrese 2 numeros para calcular la hipotenusa");
        System.out.println("ingrese un numero a");
        float a = input.nextFloat();
        System.out.println("ingrese un numero b");
        float b = input.nextFloat();
        //float hipotenusa = (a²+b²)**¹/²; ((a*a)+(b*b))
        //float hipotenusa = Math.pow(Math.pow(a,2.0f)+Math.pow(b,2.0f),1f/2f);
        double hipotenusa = Math.sqrt(Math.pow(a,2)+Math.pow(b,2));
        System.out.println("aplicando la hipotenusa de √(a²+b²) a "+a+" y "+b+" se :");
        System.out.println(hipotenusa);
        System.out.println("hi"+"po".repeat((int) hipotenusa)+"tenusa");
    }
}
