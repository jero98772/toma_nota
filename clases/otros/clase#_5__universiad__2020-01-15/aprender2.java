//import java.util.Scanner;
import javax.swing.JOptionPane;
class hola_mundo2{
    public static void main(String[] args){
	//System.out.println("di 'hello'");
	String str;
	int num;
	//Scanner entrada = new Scanner(System.in);
	//str = entrada.nextLine();
	str = JOptionPane.showInputDialog("pon un str");
	System.out.println("dijistes "+str);
	num = Integer.parseInt(JOptionPane.showInputDialog("digita tu edad"));
    }
}
//charAt guarda el primer dijito que encuentra
