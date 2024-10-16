
import java.awt.Color;
import java.awt.Graphics;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Draw a Bézier curve based on control points read from a file
 * @author htrefftz
 */
public class BezierCurve extends JPanel{
    
    public static final boolean DEBUG = false;
    public static final int FRAME_WIDTH = 500;
    public static final int FRAME_HEIGHT = 500;
    public static final int STEPS = 100;
    
    private Point [] controlPoints;
    private int numCtrlPoints = 0;
  
    public BezierCurve() {
        super();
        // El panel, por defecto no es "focusable". 
        // Hay que incluir estas líneas para que el panel pueda
        // agregarse como KeyListsener.
        this.setFocusable(true);
        this.requestFocusInWindow();

        //setBackground(Color.WHITE);
    }

    /**
     * Read:
     * n (number of control points)
     * x0, y0
     * x1, y1,
     * ...
     * xn-1, yn-1
     * @param fileName name of the file to read
     */
    public void readObjectDescription(String fileName) {
        Scanner in;
        try {
            in = new Scanner(new File(fileName));
            // Read the number of vertices
            numCtrlPoints = in.nextInt();
            controlPoints = new Point[numCtrlPoints];
            
            // Read the vertices
            for (int i = 0; i < numCtrlPoints; i++) {
                // Read a vertex
                int x = in.nextInt();
                int y = in.nextInt();
                //vertexArray[i] = new Point(x, y);
                controlPoints[i] = new Point(x, y);
            }
        } catch (FileNotFoundException e) {
            System.out.println(e);
        }

    }
    @Override
    public void keyPressed(KeyEvent e) {
      int key = e.getKeyCode();
      if(key == KeyEvent.VK_D) {
        //po.ot.dx += ObjectTransformation.DELTA_TRANSL;
        repaint();
      } else if(key == KeyEvent.VK_A) {
        //po.ot.dx -= ObjectTransformation.DELTA_TRANSL;
        repaint();
      }
    }
    @Override
    public void keyReleased(KeyEvent e) {
    }
    /**
     * Draw the axis and the curve
     * @param g Graphics context
     */
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        //Graphics2D g2d = (Graphics2D) g;
        drawAxis(g);
        
        drawCurve(g);
        
        drawPoints(g);
        
        // drawObject(g);         **
    }
    
    /**
     * Draw the control points
     * @param g2d 
     */
    private void drawPoints(Graphics g) {
        for(int i = 0; i < controlPoints.length; i++) {
            int x = (int)controlPoints[i].x;
            int y = (int)controlPoints[i].y;
            drawFatPoint(x, y, g);
        }
    }
    
    private void drawFatPoint(int x, int y, Graphics g) {
        x = x + FRAME_WIDTH/2;
        y = FRAME_HEIGHT/2 - y;
        g.setColor(Color.black);
        g.drawOval(x-1, y-1, 3, 3);
    }
    
    /**
     * Draw the Bézier curve
     * @param g2d Graphics 2D context
     */
    private void drawCurve(Graphics g) {
        g.setColor(Color.BLUE);
        Point [] points = new Point[STEPS + 1];
        double step = 1d/STEPS;
        
        double u = 0;
        for(int i = 0; i <= STEPS; i++) {
            points[i] = bezier(u, numCtrlPoints - 1);
            u += step;
        }
        
        for(int i = 0; i < STEPS; i++) {
            drawEdge(g, points[i], points[i+1]);
        }
    }

    /**
     * Draw the X and Y axis
     * @param g2d Graphics2D context
     */
    private void drawAxis(Graphics g) {
        g.setColor(Color.red);
        drawEdge(g,new Point(0, -100), new Point(0, 100));
        g.setColor(Color.green);
        drawEdge(g,new Point(-100, 0), new Point(100, 0));
    }

    /**
     * Draw a line segment. The coordinates are transformed so that
     * the origin is at the middle of the frame
     * @param g2d Graphics context
     * @param p0 inicial point
     * @param p1 final point
     */
    private void drawEdge(Graphics g,Point p0, Point p1) {
        int x0 = (int)p0.x + FRAME_WIDTH/2;
        int y0 = FRAME_HEIGHT/2 - (int)p0.y ;
        int x1 = (int)p1.x + FRAME_WIDTH/2;
        int y1 = FRAME_HEIGHT/2 - (int)p1.y;
        if(DEBUG) System.out.println("In drawEdge: " + x0 + " " + y0 + " "
            + x1 + " " + y1);
        g.drawLine(x0, y0, x1, y1);
        
    }
    
    /**
     * Compute a point for a given u in a Bézier Curve
     * @param u value of the curve parameter
     * @param n there are n+1 control points
     * @return Value of a point in the curve for given u
     */
    public Point bezier(double u, int n) {
        double acumX = 0;
        double acumY = 0;
        for(int i = 0; i < numCtrlPoints; i++) {
            double blend = blending(u, n, i);
            acumX += controlPoints[i].x * blend;
            acumY += controlPoints[i].y * blend;
        }
        return new Point(acumX, acumY);
    }
    
    /**
     * Compute the value of the blending functions at u
     * @param u value of the curve pararmeter
     * @param n there are n+1 control points
     * @param k current value of k
     * @return Value of the blending function
     */
    public double blending(double u, int n, int k) { 
        // Insert your code here
        double bez = 1;
        bez = coeff(n, k) * Math.pow(u, k) * Math.pow(1 - u, n - k);    // ***
        return bez;
    }
    
    /**
     * Compute binomial coefficients
     * @param n
     * @param k
     * @return 
     */
    public int coeff(int n, int k) {
        // Insert your code here
        int c = 1;
        c = fact(n) / (fact(k)* fact(n-k));
        return c;
    }
    
    /**
     * Compute factorial
     * @param n
     * @return 
     */
    public int fact(int n) {
        int acum = 1;
        for(int i = 1; i <= n; i++) {
            acum *= i;
        }
        return acum;
    }
    
    public static void main(String[] args) {
        if(DEBUG) System.out.println("Comenzando el programa...");
        BezierCurve bc = new BezierCurve();

        // Read the file with the object description
        bc.readObjectDescription("puntosDeControl.txt");

        // Create a new Frame
        JFrame frame = new JFrame("Curva de Bézier");
        // Upon closing the frame, the application ends
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Add a panel called DibujarCasita3D
        frame.add(bc);

        // Asignarle tamaño
        frame.setSize(500, 500);
        // Put the frame in the middle of the window
        frame.setLocationRelativeTo(null);
        // Show the frame
        frame.setVisible(true);
    }
    
}
