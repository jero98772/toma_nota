import java.util.Scanner;
public class Estrellas2{
	public static void main(String[] args){
		int[] calificaciones = new int[]{0,0,0,0,0,0}; 
		int calificacion;
		String resultados = "";
		boolean ejecutar = true;
		Scanner input = new Scanner(System.in);
		do{
			System.out.println("ingrse un numero de 0 a 5");
			calificacion = input.nextInt();
			if (calificacion<6 && calificacion>0){
				calificaciones[calificacion] = calificaciones[calificacion]+1;
			}else if (calificacion<0){
				System.out.println("bye bye");
				ejecutar = false;
				System.out.println("las calificaciones finales son:");
				for (int i = 0;i<calificaciones.length;i++){
					if (i == 0){
						resultados = "0("+calificaciones[0]+")";
					}else{
						resultados = resultados+" "+"*"*i+"("+calificaciones[i]+")";
					}
				}
				System.out.println(resultados);				
			}else{
			System.out.println("numero no valido, recuerde numeros de 0 a 5, negativos para salir");
			}
		}while(ejecutar);
	}
}