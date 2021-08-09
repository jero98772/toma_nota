//import java.util.Scanner;
public class Discoteca{
    boolean accesoDiscoteca(int edad,int dineor,String nombre){
        boolean acceso ;
        if (edad >= 18 && dinero >= 100 && nombre != "jimmy"  ){
            acceso  = true;
        }else{
            acceso = false;
        }
        return acceso;
    }
}
