public class principal{
    public static void main(){
        avion[] aviones=new avion[4];
        f35 num1f35= new f35(100,1930);
        f35 num2f35= new f35(100,1930);
        f22 num1f22= new f22(200,2414);
        f22 num2f22= new f22(200,2414);
        aviones[0]=num1f35;
        aviones[1]=num2f35;
        aviones[2]=num1f22;
        aviones[3]=num2f22;
        System.out.println(avion.infoAviones(aviones));
        System.out.println(avion.VelocidadMayor2100(aviones));
        System.out.println(avion.compararDosVelocidades(aviones[0],aviones[3]));
        avion.combate(aviones[0],aviones[1]);
        avion.combate(aviones[3],aviones[0]);
        System.out.println(avion.infoAviones(aviones));
    }
}
