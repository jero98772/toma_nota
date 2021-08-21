import java.util.Scanner;
public class ContIncrDecr{
	public static void main(String[] args){
		double num= 0;
		int contador = 0;
		double acumulado = 0;
		String msgContador = "";
		boolean aviso = true;
		Scanner input = new Scanner(System.in);
		while(aviso){
			num = input.nextDouble();
			if(num == 0){
			  	System.out.println("Contador: "+contador);
			    aviso = false;
			    break;
			}else{
			    if (num < acumulado){
			    	acumulado = num;
		    		contador=contador-1;
			    //msgContador = msgContador+"-1\n";
			        System.out.println("-1");
		    	}else{
    				acumulado = num;
				//msgContador = msgContador+"+1\n";
	    			contador=contador+1; 
		    	    System.out.println("+1");
			    }
    		}//while(num!=0);
	    }//System.out.println(msgContador);
	}
}