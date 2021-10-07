import java.util.Scanner;
class GananciaColombianos{
		public static void main(String[] args){
		boolean controlador = true;
		String pais;
		double salario,salarioAcumulado;
		Scanner input = new Scanner(System.in); 
		while(controlador){
			System.out.println("ingrse su pais:");
			pais = input.next();
			salario = input.nextDouble();
			if (pais.equals("Colombia")){
				salarioAcumulado = salarioAcumulado+salario;
			}else if(pais.equals("Bolivia") && salario<=0){
				controlador = false;
				break;
			}
			else{			
				System.out.println("Salario acumulado colombianos "+salarioAcumulado)
			}
		}
	}
}