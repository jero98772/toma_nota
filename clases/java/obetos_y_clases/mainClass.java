public class productoSimple{
    int precio;
    public int getPrecio(){
        return precio = 1000;
    }
}
public class mainClass{
    public static void main(String[] args){
        productoSimple ps = new productoSimple();
        System.out.println(ps.getPrecio());
    }
}
