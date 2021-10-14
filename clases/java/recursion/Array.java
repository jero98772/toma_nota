public class Array{
	public static void recorrerArray(int[] n,int indice){
        System.out.println(n[indice]);
		if(indice>=n.length){
		}
		else{
		    recorrerArray(n,indice+1);
		}
	}
}