public class Balanceado{
	public static boolean balancear(int[] a){
	int mitadmayor=0;
	int mitadmenor=0;
	int mitad=(a.length-1)/2; 
	for(int i=0;i<mitad;i++){
		mitadmayor=mitadmayor+a[(mitad+i)+1];
		mitadmenor=mitadmenor+a[i]; 
		}
    //System.out.println(mitadmayor);
    //System.out.println(mitadmenor);
	if(mitadmenor==mitadmayor){
		return true;	
    }else if(mitadmenor!=mitadmayor){
		return false;
	}else{
		return false;	
	}
	}
}