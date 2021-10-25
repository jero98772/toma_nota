public class Orco extends Monstruo{
	protected String grunyido;	
	public Orco(String nombre,int sangre,String grunyido){
		super(nombre,sangre);
		this.grunyido=grunyido;
	}
	public void imprimirNombre(){
		System.out.println(super.getNombre());
	}
}