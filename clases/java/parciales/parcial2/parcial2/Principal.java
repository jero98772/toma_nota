public class Principal{
    public static Tanque[] tanques=new Tanque[3];
    public static void main(String[] args){
        Tanque tanque1=new Tanque();
        Tanque tanque2=new Tanque(1002,15,15);
        Tanque tanque3=new Tanque(1003,10,8);
        tanques[0]=tanque1;
        tanques[1]=tanque2;
        tanques[2]=tanque3;
        Tanque.mostrarTanquesVivos(tanques);
        Tanque.ataque(tanque1,tanque2);
        Tanque.ataque(tanque3,tanque1);
        Tanque.mostrarTanquesVivos(tanques);
    }
}
