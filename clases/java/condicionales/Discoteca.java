public class Discoteca{
    boolean accesoDiscoteca(int edad,int dinero,String nombre){
        boolean acceso ;
        if (edad >= 18 && dinero >= 100 && !nombre.equals("jimmy")){
            acceso  = true;
        }else{
            acceso = false;
        }
        return acceso;
    }
}
