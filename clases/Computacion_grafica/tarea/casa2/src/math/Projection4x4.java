package math;

public class Projection4x4 extends Matrix4x4 {
    
    public Projection4x4(double fov, double aspect, double near, double far) {
        super();
        double f = 1 / Math.tan(fov / 2);
        double d = near - far;
        set(0, 0, f / aspect);
        set(1, 1, f);
        set(2, 2, (far + near) / d);
        set(2, 3, 2 * far * near / d);
        set(3, 2, -1);
        set(3, 3, 0);
    }   

    public Projection4x4(double d) {
        super();
        matrix[3][2] = 1/d;
    }
}
