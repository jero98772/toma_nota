package math;

public class Translation4x4 extends Matrix4x4 {
    
    public Translation4x4(double tx, double ty, double tz) {
        super();
        matrix[0][3] = tx;
        matrix[1][3] = ty;
        matrix[2][3] = tz;
    }   
}
