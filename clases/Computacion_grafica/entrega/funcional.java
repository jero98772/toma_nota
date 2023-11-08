import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class CubicBezier3D extends JPanel implements KeyListener {
    private static final int WIDTH = 800;
    private static final int HEIGHT = 600;

    private double[][] controlPoints = {
            {-100, -100, -1100},
            {-100, 100, -1100},
            {-100, 100, -900},
            {100, 100, -900}
    };

    private int numPoints = 100;
    private double[][] curvePoints;

    private double rotationAngleX = 0;
    private double rotationAngleY = 0;
    private double rotationAngleZ = 0;

    public CubicBezier3D() {
        calculateCurvePoints();
        Timer timer = new Timer(100, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                repaint();
            }
        });
        timer.start();
        addKeyListener(this);
        setFocusable(true);
        setFocusTraversalKeysEnabled(false);
    }

    private void calculateCurvePoints() {
        curvePoints = new double[numPoints][3];
        for (int i = 0; i < numPoints; i++) {
            double t = (double) i / (numPoints - 1);
            double u = 1 - t;
            double tt = t * t;
            double uu = u * u;
            double uuu = uu * u;
            double ttt = tt * t;

            for (int j = 0; j < 3; j++) {
                curvePoints[i][j] = uuu * controlPoints[0][j] + 3 * uu * t * controlPoints[1][j]
                        + 3 * u * tt * controlPoints[2][j] + ttt * controlPoints[3][j];
            }
        }
    }

    private void applyRotation(double angleX, double angleY, double angleZ) {
        double cosX = Math.cos(angleX);
        double sinX = Math.sin(angleX);
        double cosY = Math.cos(angleY);
        double sinY = Math.sin(angleY);
        double cosZ = Math.cos(angleZ);
        double sinZ = Math.sin(angleZ);

        for (int i = 0; i < controlPoints.length; i++) {
            double x = controlPoints[i][0];
            double y = controlPoints[i][1];
            double z = controlPoints[i][2];

            // Rotate around X-axis
            double newY = y * cosX - z * sinX;
            double newZ = y * sinX + z * cosX;

            // Rotate around Y-axis
            double newX = x * cosY + newZ * sinY;
            newZ = -x * sinY + newZ * cosY;

            // Rotate around Z-axis
            x = newX * cosZ - newY * sinZ;
            y = newX * sinZ + newY * cosZ;

            controlPoints[i][0] = x;
            controlPoints[i][1] = y;
            controlPoints[i][2] = z;
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawCubicBezierCurve(g);
    }

    private void drawCubicBezierCurve(Graphics g) {
        for (int i = 1; i < numPoints; i++) {
            int x1 = (int) curvePoints[i - 1][0] + WIDTH / 2;
            int y1 = (int) curvePoints[i - 1][1] + HEIGHT / 2;
            int x2 = (int) curvePoints[i][0] + WIDTH / 2;
            int y2 = (int) curvePoints[i][1] + HEIGHT / 2;

            g.setColor(Color.BLUE);
            g.drawLine(x1, y1, x2, y2);
        }

        for (int i = 0; i < 4; i++) {
            int x = (int) controlPoints[i][0] + WIDTH / 2;
            int y = (int) controlPoints[i][1] + HEIGHT / 2;

            g.setColor(Color.RED);
            g.fillOval(x - 5, y - 5, 10, 10);
        }
    }

    @Override
    public void keyTyped(KeyEvent e) {
    }

    @Override
    public void keyPressed(KeyEvent e) {
        int step = 10; // Ajusta este valor según sea necesario

        if (e.getKeyCode() == KeyEvent.VK_LEFT) {
            rotationAngleY += Math.toRadians(step);
        } else if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
            rotationAngleY -= Math.toRadians(step);
        } else if (e.getKeyCode() == KeyEvent.VK_UP) {
            rotationAngleX += Math.toRadians(step);
        } else if (e.getKeyCode() == KeyEvent.VK_DOWN) {
            rotationAngleX -= Math.toRadians(step);
        } else if (e.getKeyCode() == KeyEvent.VK_Z) {
            rotationAngleZ += Math.toRadians(step);
        } else if (e.getKeyCode() == KeyEvent.VK_X) {
            rotationAngleZ -= Math.toRadians(step);
        }

        applyRotation(rotationAngleX, rotationAngleY, rotationAngleZ);
        calculateCurvePoints();
        repaint();
    }

    @Override
    public void keyReleased(KeyEvent e) {
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Cubic Bezier Curve in 3D");
        CubicBezier3D bezierPanel = new CubicBezier3D();
        frame.add(bezierPanel);
        frame.setSize(WIDTH, HEIGHT);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}