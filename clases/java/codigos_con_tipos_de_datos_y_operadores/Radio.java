import java.util.Scanner;
public class Radio {
    public static void main(String[] args){
        float pi = 3.1415926535F;
        Scanner input = new Scanner(System.in);
        System.out.println("ingrse el radio de un circulo");
        float radio = input.nextFloat();
        float area = (radio*radio)*pi;
        String areatxt = String.format("%.2f",area);
        System.out.println("el area es :" );
        System.out.println(areatxt);
    }
}