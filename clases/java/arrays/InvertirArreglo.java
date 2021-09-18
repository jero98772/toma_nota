public class InvertirArreglo{
	public int invertir(int[] a){
		int tamanoa=a.length();
		int[] nuevoArreglo = new int[tamanoa];
		for(int i=0;i<tamanoa;i++){
			nuevoArreglo[i] = a[tamanoa-i];
    }
    return nuevoArrgelo;
	}
	public void imprimir(int[] a){
		//for(int i=0;i<a.length;){System.out.println(a[i]);}
		System.out.println(a);
	}
}
