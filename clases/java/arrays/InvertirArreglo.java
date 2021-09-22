public class InvertirArreglo{
	public static int[] invertir(int[] a){
		//int tamanoa=a.length;
		int[] nuevoArreglo = new int[a.length];
		for(int i=0;i<a.length;i++){
			nuevoArreglo[i] = a[(a.length-i)-1];
    }
    return nuevoArreglo;
	}
	public static void imprimir(int[] a){
		for(int i=0;i<a.length;i++){
		    if (i==0){System.out.print(a[i]);}
		    else{System.out.print(","+a[i]);}
		}
		//System.out.println(a);
	}
}
