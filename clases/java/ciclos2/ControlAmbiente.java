import java.util.Scanner;
public class ControlAmbiente{
	public static void main(String[] args){
		 SensorActuador sa1 = new SensorActuador(5,1,10);
		 Scanner input = new Scanner(System.in);
		 int num;
		 int iterationLimit =4 ; 
		 for(int i = 0;i<iterationLimit;i++){
		 	num = input.nextInt();
		 	if(i<2){
		 		sa1.disminuirTemp(num);
		 	}else{
		 		sa1.aumentarTemp(num);
		 	}

		 }
		 System.out.println(sa1.getTemperatura());
	}
}