package math;

public class Scaling4x4 extends Matrix4x4 {

    public Scaling4x4(double sx, double sy, double sz) {
        super();
        matrix[0][0] = sx;
        matrix[1][1] = sy;
        matrix[2][2] = sz;
    }

}