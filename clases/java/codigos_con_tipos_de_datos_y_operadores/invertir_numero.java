import java.util.Scanner;
public class invertir_numero {
    public static void main(String[] args){
        System.out.println("Ingrese un numero de 3 digitos");
        Scanner input = new Scanner(System.in);
        short num = input.nextShort();
        if (99<num && num<1000){
            int unidades = num/100;
            int decenas = ((num/10)%10)*10;
            int centenas = (num*100)%1000;
            int newnum = centenas+decenas+unidades;
            System.out.println("el numero ingresado fue: "+num+"\n y el numero invertido es: "+newnum);
        }
        else{
            System.out.println("porfavor ingrese un numero de 3 digitos como 666");
        }
    }
}

