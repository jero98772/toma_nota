public class Point{
    private double x;
    private double y;
   
    public Point(){
        this.x = 0;
        this.y = 0;
    }
    public void setX(double x){
        this.x = x;
    }
    public double getX(){
        return this.x;
    }
    public void setY(double y){
        this.y = y;
    }
    public double getY(){
        return this.y;
    }
    public Point puntoMedio(Point p2){
        double xm = ((this.x+p2.getX())/2);
        double ym = ((this.y+p2.getY())/2);
        Point p3 = new Point();
        p3.setY(ym);
        p3.setX(xm);
        return p3;          
    }
}
