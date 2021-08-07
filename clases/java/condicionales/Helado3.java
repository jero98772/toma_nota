import java.util.Scanner;
class Helado3{
    public static void main(String[] args){
        int temperaturaLimite = 27;
        Scanner input = new Scanner(System.in);
        int temperaturaActual = input.nextInt();
        int edad = input.nextInt();
        if (temperaturaActual > temperaturaLimite && edad > 18){
            int costo = 5000;
            int dinero = input.nextInt();
            if (dinero < costo){
                System.out.println("Comprar helado cerveza");
                }
            else{
                System.out.println("De que me hablas viejo");
            }
        }
        else{
            System.out.println("Lo sentimos juventud");
        }
    }
}
