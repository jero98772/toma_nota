class Planeta{
	private String nombre;
	private double masa;
	public int contador=0;
	public Planeta(){
		Planeta planet=new Planeta("Tierra",5.972);
	}
	public Planeta(String n,double m){
		this.nombre=n;
		this.masa=m;	
	}
	public String getNombre(){
		return	this.nombre;
	}
	public double getMasa(){
		return	this.masa;
	}
	public void setNombre(String n){
		return	this.nombre = n;
	}
	public void setMasa(double m){
		return	this.masa = m;
	}
	public Planeta planetaMedio(Planeta p){
		double masaPlanetaP = (p.getMasa()/2);
		String nombrePlanetaP = p.getNombre();		
		Planeta nuevoPlaneta=new Planeta(nombrePlanetaP,masaPlanetaP);
	}
}