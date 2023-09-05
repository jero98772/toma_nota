package math;

public class RotationX4x4 extends Matrix4x4 {
    
    public RotationX4x4(double theta) {
        super();
        matrix[1][1] = Math.cos(theta);
        matrix[1][2] = -Math.sin(theta);
        matrix[2][1] = Math.sin(theta);
        matrix[2][2] = Math.cos(theta);
    }
}
