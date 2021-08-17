import java.util.Scanner;
public class Estrellas{
	public static void main(String[] args){
		int[] calificaciones = new int[]{0,0,0,0,0,0}; 
		int calificacion;
		int cantidad = 0;
		String resultados = "";
		boolean ejecutar = true;
		Scanner input = new Scanner(System.in);
		do{
			//System.out.println("ingrse un numero de 0 a 5");
			calificacion = input.nextInt();
			if (calificacion<6 && calificacion>-1){
				calificaciones[calificacion] = calificaciones[calificacion]+1;
				//cantidad = cantidad +1;
				cantidad++;
			}else if (calificacion<0){
				//System.out.println("bye bye");
				ejecutar = false;
				//System.out.println("las calificaciones finales son:");
				System.out.println("0("+calificaciones[0]+") *("+calificaciones[1]+") **("+calificaciones[2]+") ***("+calificaciones[3]+") ****("+calificaciones[4]+") *****("+calificaciones[5]+")");
				System.out.println("Total: "+cantidad);
				/*for (int i = 0;i<calificaciones.length;i++){
					if (i == 0){
						resultados = "0("+calificaciones[0]+")";
					}else{
						resultados = resultados+" "+"*".repeat(i)+"("+calificaciones[i]+")";
					}
				}*/
				System.out.println(resultados);				
			}else{
			//System.out.println("numero no valido, recuerde numeros de 0 a 5, negativos para salir");
			}
		}while(ejecutar);
	}
}