class Punto{
	private double x;
	private double y;
	Punto(double x,double y){
			this.x = x;
			this.y = y;
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
	static double distancia(Punto p,Punto p2){
	    double powX = Math.pow(p2.getX()-p.getX(),2);
	    double powY = Math.pow(p2.getY()-p.getY(),2);
		double result = Math.sqrt(powX+powY);
		return	result;
	}
}