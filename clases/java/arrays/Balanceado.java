public class Balanceado{
	public static void baleancear(int[] a){
	int mitad,mitadmayor,mitadmenor
	mitad=(a.length-1)/2; 
	for(int i=0;i<mitad;i++){
		mitadmayor=mitadmayor+a[i]
		mitadmenor=mitadmenor+a[mitad-i] 
		}  
	if(mitadmenor==mitadmayor){
		return true;	
	}else{
		return false;	
	}
	}
}