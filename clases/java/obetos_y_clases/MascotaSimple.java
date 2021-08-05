public class MascotaSimple{
    private int edad =8;
    private String nombre;
    public MascotaSimple(String nuevoNombre){
        this.nombre = nuevoNombre;
    }
    public MascotaSimple(String nuevoNombre,int nuevaEdad){
        this.nombre = nuevoNombre;
        this.edad = nuevaEdad;
    }
    public String getNombre(){
        return this.nombre;
    }
    public int getEdad(){
        return this.edad;
    }
    public MascotaSimple() {
    this.nombre = "kitty";
    }
}

