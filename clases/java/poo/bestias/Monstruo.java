public class Monstruo{
    protected String nombre;
    protected int sangre;
    public Monstruo(String nombre,int sangre){
        this.nombre=nombre;
        this.sangre=sangre;
    }
    public void moverse(){
        System.out.println("Soy un monstruo que se mueve lento "+this.nombre);
    }
    public String getNombre(){
        return this.nombre;
    }
    public int getSangre(){
        return this.sangre; 
    }
    public void setNombre(String nombre){
        this.nombre=nombre;
    }
    public void setSangre(int sangre){
        this.sangre=sangre;
    }
}
