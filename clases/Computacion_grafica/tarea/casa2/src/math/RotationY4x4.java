package math;

public class RotationY4x4 extends Matrix4x4 {
    
    public RotationY4x4(double theta) {
        super();
        matrix[0][0] = Math.cos(theta);
        matrix[0][2] = Math.sin(theta);
        matrix[2][0] = -Math.sin(theta);
        matrix[2][2] = Math.cos(theta);
    }
}
