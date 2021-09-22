public class MayorQue{
	public static void mayor(int[] a){
		boolean noHayMayor=true;
		int mayor=a[0];
		//System.out.println(a[1]);
		for(int i=0;i<a.length;i++){
			if(mayor<a[i]){
				System.out.println(a[i]);
                noHayMayor=false;
			}
    	}if(noHayMayor){
		  System.out.println("No hay ningun numero mayor que el primero");
		}
	}
}