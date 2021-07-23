import java.util.Scanner;
public class FriendZone{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Ingrse el nombre de una persona");
        String nombre1 = input.nextLine();
        System.out.println("Ingrse el nombre del amig@ de "+nombre1);
        String nombre2 = input.nextLine();
        System.out.println(nombre2+ " dejo en la friendzone a "+nombre1);
        
    }
}
