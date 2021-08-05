import java.util.Scanner;
class Helado{
    public static void main(String[] args){
        int temperaturaLimite = 27;
        Scanner input = new Scanner(System.in);
        int temperaturaActual = input.nextInt();	
        if (temperaturaActual > temperaturaLimite){
            System.out.println("Comprar helado cerveza");
        }
    }
}
