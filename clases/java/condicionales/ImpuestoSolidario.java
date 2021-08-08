import java.util.Scanner;
public class ImpuestoSolidario{
	public static void main(String[] args){
		double impuesto = 15;
		Scanner input = new Scanner(System.in);
		System.out.println("ingrese su salario:\n");	
		double salario = input.nextDouble();
		System.out.println("ingrese su tipo de contrato [publico/privado]");
		String contrato = input.next();
		if (contrato.equals("publico") && salario > 10000000){
			double valorAPagar = (salario/100)*impuesto;
			System.out.println(String.format("%.2f",valorAPagar));
		}else{
			System.out.println("No debes aportar");
		}
	}
}
