public class MayorQue{
	public static void main(int[] a){
		int menor=a[0];
		for(int i=1;i<a.lenth;i++){
			if(a[i]<menor){
				menor = a[i];
			}else{
				System.out.println(a[i]);
			}
		}
	}
}