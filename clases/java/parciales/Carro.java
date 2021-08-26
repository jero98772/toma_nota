class Carro{
	String marca;
	boolean encendio = true;
	int velocidad = 0;
	int velocidadMaxima =100;
	public Carro(String marc){
		this.marca = marc;
	}
	public Carro(String marc,boolean enced){
		this.marca = marc;
		this.encendio = enced;
	}
	public String getMarca(){
		return this.marca;
	}
	public int getVelocidad(){
		return this.velocidad;
	}
	public boolean getEncendido(){
		return this.encendio;
	}
	public void apagar(){
		this.encender = false;
	}
	public void encender(){
		this.encendio = true;
	}
	public void aumentarVelocidad(int v){
		if (this.velocidad+v>=this.velocidadMaxima && this.encendio){
			this.velocidad = this.velocidad-v;
		}
	}
	public void disminuirVelocidad(int v){
		if (this.velocidad-v>=0 &&  this.encendio){
			this.velocidad = this.velocidad-v;
		}
	}
}