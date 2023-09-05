package math;

public class RotationZ4x4 extends Matrix4x4 {
    public RotationZ4x4(double theta) {
        super();
        matrix[0][0] = Math.cos(theta);
        matrix[0][1] = -Math.sin(theta);
        matrix[1][0] = Math.sin(theta);
        matrix[1][1] = Math.cos(theta);
    }
}
