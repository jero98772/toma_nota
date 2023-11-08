import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;

public class CubicBezierCurve3D extends JPanel {

    private ArrayList<Point3D> controlPoints = new ArrayList<>();

    private static class Point3D {
        double x, y, z;

        public Point3D(double x, double y, double z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }
    }

    public CubicBezierCurve3D() {
        controlPoints.add(new Point3D(-100,-100,-1100));
        controlPoints.add(new Point3D(-100,100,-1100));
        controlPoints.add(new Point3D(-100,100,-900));
        controlPoints.add(new Point3D(100,100,-900));
    }

    // Cubic Bezier interpolation
    private Point3D cubicBezier(double t) {
        double x = (1 - t) * (1 - t) * (1 - t) * controlPoints.get(0).x +
                3 * t * (1 - t) * (1 - t) * controlPoints.get(1).x +
                3 * t * t * (1 - t) * controlPoints.get(2).x +
                t * t * t * controlPoints.get(3).x;

        double y = (1 - t) * (1 - t) * (1 - t) * controlPoints.get(0).y +
                3 * t * (1 - t) * (1 - t) * controlPoints.get(1).y +
                3 * t * t * (1 - t) * controlPoints.get(2).y +
                t * t * t * controlPoints.get(3).y;

        double z = (1 - t) * (1 - t) * (1 - t) * controlPoints.get(0).z +
                3 * t * (1 - t) * (1 - t) * controlPoints.get(1).z +
                3 * t * t * (1 - t) * controlPoints.get(2).z +
                t * t * t * controlPoints.get(3).z;

        return new Point3D(x, y, z);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        g2.setColor(Color.BLUE);

        int steps = 100;
        Point3D[] curvePoints = new Point3D[steps];
        for (int i = 0; i < steps; i++) {
            double t = i / (double) steps;
            curvePoints[i] = cubicBezier(t);
        }

        for (int i = 0; i < steps - 1; i++) {
            g2.drawLine((int) curvePoints[i].x, (int) curvePoints[i].y, (int) curvePoints[i + 1].x, (int) curvePoints[i + 1].y);
        }

        g2.setColor(Color.RED);
        for (Point3D point : controlPoints) {
            g2.fillRect((int) point.x, (int) point.y, 5, 5);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Cubic Bezier Curve in 3D");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(1600, 1000);
            CubicBezierCurve3D curvePanel = new CubicBezierCurve3D();
            frame.add(curvePanel);
            frame.setVisible(true);
        });
    }
}
