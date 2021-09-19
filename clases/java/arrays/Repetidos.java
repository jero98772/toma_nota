import java.util.ArrayList;
public class Repetidos{
	public static int detectorDeRepetidos(ArrayList<Integer> a){
		int i=1;
		int suceciones=0;
		int valorAnterior=a.get(0);
		boolean leido=true;
		do{
		    if(valorAnterior == a.get(i)){
		        if(leido){
                    suceciones=suceciones+1;   
                    leido=false;
		        }
			}else{
			    leido=true;
			}
			valorAnterior = a.get(i);
		    i=i+1;
		}while(i<a.size());
		//System.out.println(suceciones);
	    return suceciones;
	}
}