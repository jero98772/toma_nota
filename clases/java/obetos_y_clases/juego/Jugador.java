public class Jugador{
    private String nombre;
    private int sauld;
    public void setNombre(String n){
        this.nombre = n;
    }
    public void setSalud(int s){
        this.salud = s;
    }
    public String getNombre(){
        return this.nombre;
    }
    public int getSalud(){
        return this.salud;
    }
    public void reducirSalud(int s){
	this.salud = this.salud - s;
    }
}
