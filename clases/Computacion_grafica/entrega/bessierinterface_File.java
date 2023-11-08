import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class CubicBezierCurve3D extends JPanel {

    private static final int POINT_SIZE = 8;
    private static final int CURVE_RESOLUTION = 100;
    private Point3D[] controlPoints = new Point3D[4];
    private int selectedPointIndex = -1;

    private static class Point3D {
        double x, y, z;

        public Point3D(double x, double y, double z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }
    }

    public CubicBezierCurve3D() {
        controlPoints[0] = new Point3D(-100, -100, -1100);
        controlPoints[1] = new Point3D(-100, 100, -1100);
        controlPoints[2] = new Point3D(-100, 100, -900);
        controlPoints[3] = new Point3D(100, 100, -900);

        addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                for (int i = 0; i < controlPoints.length; i++) {
                    int x = (int) controlPoints[i].x + getWidth() / 2;
                    int y = getHeight() / 2 - (int) controlPoints[i].y;
                    if (Math.abs(x - e.getX()) <= POINT_SIZE && Math.abs(y - e.getY()) <= POINT_SIZE) {
                        selectedPointIndex = i;
                        break;
                    }
                }
            }

            @Override
            public void mouseReleased(MouseEvent e) {
                selectedPointIndex = -1;
            }
        });

        addMouseMotionListener(new MouseAdapter() {
            @Override
            public void mouseDragged(MouseEvent e) {
                if (selectedPointIndex != -1) {
                    controlPoints[selectedPointIndex].x = e.getX() - getWidth() / 2;
                    controlPoints[selectedPointIndex].y = getHeight() / 2 - e.getY();
                    repaint();
                }
            }
        });
    }

    private Point3D cubicBezier(double t) {
        double x = (1 - t) * (1 - t) * (1 - t) * controlPoints[0].x +
                3 * t * (1 - t) * (1 - t) * controlPoints[1].x +
                3 * t * t * (1 - t) * controlPoints[2].x +
                t * t * t * controlPoints[3].x;

        double y = (1 - t) * (1 - t) * (1 - t) * controlPoints[0].y +
                3 * t * (1 - t) * (1 - t) * controlPoints[1].y +
                3 * t * t * (1 - t) * controlPoints[2].y +
                t * t * t * controlPoints[3].y;

        double z = (1 - t) * (1 - t) * (1 - t) * controlPoints[0].z +
                3 * t * (1 - t) * (1 - t) * controlPoints[1].z +
                3 * t * t * (1 - t) * controlPoints[2].z +
                t * t * t * controlPoints[3].z;

        return new Point3D(x, y, z);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;

        int steps = CURVE_RESOLUTION;
        Point3D[] curvePoints = new Point3D[steps];
        for (int i = 0; i < steps; i++) {
            double t = i / (double) steps;
            curvePoints[i] = cubicBezier(t);
        }

        for (int i = 0; i < steps - 1; i++) {
            g2.setColor(Color.BLUE);
            g2.setStroke(new BasicStroke(2));
            g2.drawLine((int) curvePoints[i].x, (int) curvePoints[i].y, (int) curvePoints[i + 1].x, (int) curvePoints[i + 1].y);
        }

        g2.setColor(Color.RED);
        for (Point3D point : controlPoints) {
            int x = (int) point.x + getWidth() / 2;
            int y = getHeight() / 2 - (int) point.y;
            g2.fillRect(x - POINT_SIZE / 2, y - POINT_SIZE / 2, POINT_SIZE, POINT_SIZE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Cubic Bezier Curve in 3D");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(800, 600);
            CubicBezierCurve3D curvePanel = new CubicBezierCurve3D();
            frame.add(curvePanel);
            frame.setVisible(true);
        });
    }
}
 
