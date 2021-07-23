import java.util.Scanner;
public class Asteroides{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Ingrese el Nombre de los asteroides:");
        String nombresAsteroides = input.nextLine();
        System.out.println("Ingrse la cantidad de asteroides:");
        short cantidadAsteroides = input.nextShort();
        System.out.println("los "+cantidadAsteroides+" Asteroides "+nombresAsteroides+" caen del cielo");
    }
}
