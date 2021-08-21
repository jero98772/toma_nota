public class SensorActuador{
	private int temperatura;
	private int maxTemp;
	private int minTemp;
	public SensorActuador(int temp , int min , int max){
	this.temperatura = temp;
	this.minTemp = min;
	this.maxTemp = max;
	}
	int getTemperatura(){
		return this.temperatura;
	}
	void disminuirTemp(int valor){
		if ((this.temperatura-valor)>=this.minTemp){
			this.temperatura = this.temperatura-valor;
		}
	}
	void aumentarTemp(int valor){
		if (((this.temperatura+valor)<=this.maxTemp)){
			this.temperatura = this.temperatura+valor;
		}

	}
}