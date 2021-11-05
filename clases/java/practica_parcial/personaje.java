public class personaje{
    private String nombre;
    private int salud;
    private int ataque;
    personaje(){}
    personaje(String n,int s,int a){
        this.nombre=n;
        this.salud=s;
        this.ataque=a;
    }
    public String getNombre(){
        return this.nombre;
    }
    public int getsalud(){
        return this.salud;
    }
    public int getAtaque(){
        return this.ataque;
    }
    public void setNombre(String n){
        this.nombre=n;
    }
    public void setSalud(int s){
        this.salud=s;
    }
    public void setAtaque(int a){
        this.ataque=a;
    }
    public static void mostrarNombresPersonajes(personaje[] personajes){
        for(int i=0;i<personajes.length;i++){
            System.out.println(personajes[i].getNombre());
        }
    }
}