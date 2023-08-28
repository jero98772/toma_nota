import javax.swing.*;
import java.awt.*;
import java.util.*;  
import java.awt.event.KeyListener;
import math.*;

public class casa extends JPanel {
  public ArrayList<points3> puntos = new ArrayList<>();  
  static Integer centrarX(Integer x,Integer w){
    return x+w/2;
  }
  static Integer centrarY(Integer y,Integer h){
    return h/2-y;
  }
  static points3 centrarPunto(Integer x,Integer y,Integer witdth,Integer height){
    Integer newX=centrarY(y,height);
    Integer newY=centrarX(x,witdth);
    points3 newPoint=new points3(newX,newY,1);
    return newPoint;
  }
  /*@Override
  public void keyPressed(KeyEvent e) {
      int tecla = e.getKeyCode();
      //System.out.println("Key pressed");
      if(tecla == KeyEvent.VK_UP) {
          ovalo1.y -= 20;
      } else if (tecla == KeyEvent.VK_DOWN) {
          ovalo1.y += 20;
      } else if (tecla == KeyEvent.VK_RIGHT) {
          ovalo1.x += 20;
      } else if(tecla == KeyEvent.VK_LEFT) {
          ovalo1.x -= 29;
      }
      repaint();    
  }

  
    public casa() {
        // El panel, por defecto no es "focusable". 
        // Hay que incluir estas líneas para que el panel pueda
        // agregarse como KeyListsener.
        this.setFocusable(true);
        this.requestFocusInWindow();

        this.addKeyListener(this);
    }
    */
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        int panelWidth = getWidth();
        int panelHeight = getHeight();

        // Dibuja el eje X en rojo
        g.setColor(Color.RED);
        g.drawLine(0, panelHeight / 2, panelWidth, panelHeight / 2);

        // Dibuja el eje Y en verde
        g.setColor(Color.GREEN);
        g.drawLine(panelWidth / 2, 0, panelWidth / 2, panelHeight);

  
        // Dibuja la casita centrada

        g.setColor(Color.BLACK);

        g.drawLine(panelWidth / 2 - 50, panelHeight / 2- -50, panelWidth / 2 + 50, panelHeight / 2- -50);
        g.drawLine(panelWidth / 2 - 50, panelHeight / 2 - 50, panelWidth / 2 + 50, panelHeight / 2 - 50);
        g.drawLine(panelWidth / 2, panelHeight / 2 - 100, panelWidth / 2 + 50, panelHeight / 2 - 50);
        g.drawLine(panelWidth / 2 - 50, panelHeight / 2 - 50, panelWidth / 2, panelHeight / 2 - 100);
        g.drawLine(panelWidth / 2 + 50, panelHeight / 2 - 50, panelWidth / 2 + 50, panelHeight / 2 + 50);
        g.drawLine(panelWidth / 2 - 50, panelHeight / 2 - 50, panelWidth / 2 - 50, panelHeight / 2 + 50);

        // Dibuja la casita trasladada

        g.setColor(Color.BLUE);
        //mas 100 por que +100 en x
        g.drawLine(panelWidth / 2 - 50+100, panelHeight / 2- -50-50, panelWidth / 2 + 50+100, panelHeight / 2- -50-50);
        g.drawLine(panelWidth / 2 - 50+100, panelHeight / 2 - 50-50, panelWidth / 2 + 50+100, panelHeight / 2 - 50-50);
        g.drawLine(panelWidth / 2 + 50+100, panelHeight / 2 - 50-50, panelWidth / 2 + 50+100, panelHeight / 2 + 50-50);
        g.drawLine(panelWidth / 2 - 50+100, panelHeight / 2 - 50-50, panelWidth / 2 - 50+100, panelHeight / 2 + 50-50);
        g.drawLine(panelWidth / 2 - 50+100, panelHeight / 2- -50-50, panelWidth / 2 + 50+100, panelHeight / 2- -50-50);
        g.drawLine(panelWidth / 2 +100 , panelHeight / 2 - 100-50, panelWidth / 2 + 50+100, panelHeight / 2 - 50-50);//este
        g.drawLine(panelWidth / 2 - 50+100, panelHeight / 2 - 50-50, panelWidth / 2+100, panelHeight / 2 - 100-50);

        
    }
/*    @Override
    public void keyReleased(KeyEvent e) {}
    @Override
    public void keyTyped(KeyEvent e) {}*/
    public static void main(String[] args) {
        JFrame frame = new JFrame("Dibujar Casita Centrada");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new casa());
        frame.setSize(400, 400);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
