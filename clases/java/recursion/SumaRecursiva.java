public class SumaRecursiva{
	public static int sumaRecursiva(int n){
		if(n==0){
			return n;
		}else{
			return n+sumaRecursiva(n-1);
		}
	}
}