class Punto(){
	private double x;
	private double y;
	Punto(double x,double y){
			
	}
	double getX(){
		return this.x;	
	}
	double getY(){
		return this.y;	
	}
	void setX(double x){
		this.x = x;
	}
	void setY(double y){
		this.y = y;
	}
	static double distancia(double x,double y){
		double result = math.sqrt(math.pow(x+y,2)
		return	result;
	}
}