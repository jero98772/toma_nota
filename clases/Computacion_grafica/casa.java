import java.io.File;  
import java.io.FileNotFoundException;
import java.util.Scanner; 
import javax.swing.*;
import java.awt.*;
import java.util.*;  
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import math.*;
import transformations.*;

public class casa extends JPanel implements KeyListener {
  static ArrayList<points3> puntos = new ArrayList<>();  
  static ArrayList<points3> conexiones = new ArrayList<>();
  static int height=600;
  static int width=600;
  static int centerX=0;
  static int centerY=0;
  static int moveC=5;
  static Integer centrarX(Integer x,Integer w){
    return x+w/2;
  }
  static Integer centrarY(Integer y,Integer h){
    return h/2-y;
  }

  static points3 centrarPunto(Integer x,Integer y,Integer witdth,Integer height){
    Integer newX=centrarX(x,witdth);
    Integer newY=centrarY(y,height);
    points3 newPoint=new points3(newX,newY,1);
    return newPoint;
  }
  @Override
public void keyPressed(KeyEvent e) {
    int keyCode = e.getKeyCode();
    if (keyCode == KeyEvent.VK_A) {
        System.out.println("A");
        // Handle left arrow key
        Move.makeMove(-1*moveC, 0, puntos);
        repaint(); // Repaint the panel to reflect the changes
    } else if (keyCode == KeyEvent.VK_D) {
        // Handle right arrow key
        System.out.println("D");
        Move.makeMove(moveC, 0, puntos);
        repaint();
    } else if (keyCode == KeyEvent.VK_W) {
        System.out.println("W");
        // Handle up arrow key
        Move.makeMove(0, moveC, puntos);
        repaint();
    } else if (keyCode == KeyEvent.VK_S) {
        // Handle down arrow key
        System.out.println("S");
        Move.makeMove(0, -1*moveC, puntos);
        repaint();
    }else if (keyCode == KeyEvent.VK_E){
      System.out.println("E");
      Rotate.makeRotation(-1, puntos);
      repaint();
    }else if (keyCode == KeyEvent.VK_Q){
      //rotate
      System.out.println("Q");
      Rotate.makeRotation(1, puntos);
      repaint();
    }else if (keyCode == KeyEvent.VK_M){
      //zoom in
      System.out.println("M");
      Zoom.makeZoom(1.1, puntos);
      repaint();

    }else if (keyCode == KeyEvent.VK_N){
      //zoom out
      System.out.println("N");
      Zoom.makeZoom(0.9, puntos);
      repaint();
    }
}

@Override
public void keyReleased(KeyEvent e) {
    // Handle key release if needed
}

@Override
public void keyTyped(KeyEvent e) {
    // Handle key typed if needed
}

    static void paint(Graphics g,int panelWidth,int panelHeight){
        for (int i=0;i<conexiones.size();i++){
          points3 con=conexiones.get(i);
          points3 point1=puntos.get(con.getx());
          points3 point2=puntos.get(con.gety());
          int x1=centrarX(point1.getx(),panelWidth);
          int y1=centrarY(point1.gety(),panelHeight);
          int x2=centrarX(point2.getx(),panelWidth);
          int y2=centrarY(point2.gety(),panelHeight);
          g.drawLine(x1,y1,x2,y2);
        } 

    }
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        width = getWidth();
        height = getHeight();
        int panelWidth = getWidth();
        int panelHeight = getHeight();

        // Dibuja el eje X en rojo
        g.setColor(Color.RED);
        g.drawLine(0, panelHeight / 2, panelWidth, panelHeight / 2);

        // Dibuja el eje Y en verde
        g.setColor(Color.GREEN);
        g.drawLine(panelWidth / 2, 0, panelWidth / 2, panelHeight);

        g.setColor(Color.BLACK);
        paint(g,panelWidth, panelHeight);
        //Move.makeMove(100, 50, puntos);
        //paint(g,panelWidth, panelHeight);
    }
    public static void main(String[] args) {

        JFrame frame = new JFrame("Dibujar Casita Centrada");
        String filename="casita.txt";
        try {
          File myObj = new File(filename);
          Scanner myReader = new Scanner(myObj);
          int nodes = Integer.parseInt(myReader.nextLine());
          String nodo,edge;
          for(int i=0;i<nodes;i++){
            nodo = myReader.nextLine();
            String[] parts = nodo.split(" ");
            points3 newPoint= new points3(Integer.parseInt(parts[0]),Integer.parseInt(parts[1]),0);
            puntos.add(newPoint);
          }
          int edges = Integer.parseInt(myReader.nextLine());
          for(int i=0;i<edges;i++){
            edge = myReader.nextLine();
            String[] parts = edge.split(" ");
            
            points3 newEdge=new points3(Integer.parseInt(parts[0]),Integer.parseInt(parts[1]),0);
            conexiones.add(newEdge) ;
          }

          myReader.close();
          } catch (FileNotFoundException e) {
          System.out.println("An error occurred.");
          e.printStackTrace();
        }

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        casa casaPanel = new casa();
        frame.addKeyListener(casaPanel);
        frame.setFocusable(true); 
        frame.requestFocus(); 
        frame.add(casaPanel);

        //frame.add(new casa());
        frame.setSize(width, height);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
