package math;

public class TranslScalRot4x4 extends Matrix4x4 {

    double dx = 0;
    double dy = 0;
    double dz = 0;
    double sx = 1;
    double sy = 1;
    double sz = 1;
    double thetaX = 0;
    double thetaY = 0;
    double thetaZ = 0;
    double centerX = 0;
    double centerY = 0;
    double centerZ = 0;

    public TranslScalRot4x4() {
        super();
    }

    public TranslScalRot4x4(double dx, double dy, double dz,
            double sx, double sy, double sz,
            double thetaX, double thetaY, double thetaZ,
            double centerX, double centerY, double centerZ) {
        super();

    }
    
}