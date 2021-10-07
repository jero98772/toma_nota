public class Tanque
{
    private int codigo;
    private int ataque;
    private int salud;
    public Tanque(){
     Tanque tanque=new Tanque(1001,4,8);
    }
    Tanque(int c,int a,int s){
        this.codigo=c;
        this.ataque=a;
        this.salud=s;
    }
    public static void ataque(Tanque t1,Tanque t2){
        t2.setSalud(t2.getSalud()-t1.getAtaque());
        if(t2.getSalud()<1){// si no puede ser mayor , puede ser menor , para ahorrarse el else
            System.out.println("tanque "+t2.getCodigo()+" fue destrido");
        }         
    }public int getSalud(){
        return this.salud;
    }public int getCodigo(){
        return this.codigo;
    }public int getAtaque(){
        return this.ataque;
    }public void setCodigo(int c){
        this.codigo=c;
    }public void setAtaque(int a){
        if(a>=0){
            this.ataque=a;
        }
    }public void setSalud(int s){
        this.salud=s;
    }public String toString(){
        String txt="codigo:"+this.codigo+"\nsalud:"+this.salud+"\nataque:"+this.ataque;
        return txt;
    }
    public static void mostrarTanquesVivos(Tanque[] tanques){
        for(int i=0;i<tanques.length;i++){
            if(tanques[i].getSalud()>0){
                tanques[i].toString();
            }
        }
    }
}
