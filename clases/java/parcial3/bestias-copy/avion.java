public class avion{
    private int velocidad;
    private int costo;
    private int salud;
    private int ataque;
    public avion(){
    }
    public avion(int c,int v,int s,int a){
        this.velocidad=v;
        this.costo=c;
        this.salud=s;
        this.ataque=a;
    }
    public String toString(){
        return "salud"+this.salud+",velocidad:"+this.velocidad+",costo:"+this.costo+"  ";
    }
    public static String compararDosVelocidades(avion a1,avion a2){
        if(a1.getVelocidad()<a2.getVelocidad()){
            return a2.toString();
        }else{
            return a1.toString();
        }
    }
    public static String VelocidadMayor2100(avion[] aviones){
        String avionesTxt="";
        for(int i=0;i<aviones.length;i++){
            if(aviones[i].getVelocidad()>2100){
                avionesTxt=avionesTxt+aviones[i].toString();
            }
        }
        return avionesTxt;
    }
    public static String infoAviones(avion[] aviones){
        String avionesTxt="";
        for(int i=0;i<aviones.length;i++){
                avionesTxt=avionesTxt+aviones[i].toString();
        }
        return avionesTxt;
    }
    public static void combate(avion a1,avion a2){
         a2.setSalud(a2.getSalud()-a1.getAtaque());
    }
    public int getVelocidad(){
        return this.velocidad;
    }
    public int getSalud(){
        return this.salud;
    }
    public int getCosto(){
        return this.costo;
    }
    public int getAtaque(){
        return this.ataque;
    }
    public void setVelocidad(int cambio){
        this.velocidad=cambio;
    }
    public void setAtaque(int cambio){
        this.ataque=cambio;
    }
    public void setCosto(int cambio){
        this.costo=cambio;
    }
    public void setSalud(int cambio){
        this.salud=cambio;
    }
}
