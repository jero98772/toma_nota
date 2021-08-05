import java.util.Scanner;
class x2{
    public static void main(String[] args){
        int calorEs = 27;
        int frioEs = 20;
        Scanner input = new Scanner(System.in);
        System.out.println("ingrese la temperatura:");
        int temperature = input.nextInt();
        if (frioEs<temperature &&  temperature < calorEs){
        //if (frioEs < temperature < calorEs){
         System.out.println("hace calor");
        }
        System.out.println("fin");
    }
}
