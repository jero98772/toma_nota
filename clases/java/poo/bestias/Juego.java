public class Juego{
    private Monstruo[] monstruos=new Monstruo[4];
    public Juego(){
        Orco orco1=new Orco("Garnag",10,"grrr");
        Dragon dragon1=new Dragon("Brenton",20,"metal");
        Orco orco2=new Orco("Rogthun",5,"purr");
        Dragon dragon2=new Dragon("Shenlong",40,"cuero");
        monstruos[0]=orco1;
        monstruos[1]=dragon1;
        monstruos[2]=orco2;
        monstruos[3]=dragon2;
    }
    public void moverMonstruos(){
        for(int i=0;i<monstruos.length;i++){
            monstruos[i].moverse();
        }
    }
}
