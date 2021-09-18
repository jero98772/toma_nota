public class Sortario{
	public static void detectorDeMalaSuerte(int[] a){
	boolean tiene1,tiene3,tiene13;
	for(int i=0;i<a.length();i++){
		if(a[i]==1){tiene1=true}
		if(a[i]==3){tiene3=true}
		if(a[i]==13){tiene13=true}
	}if((tiene1&&tiene3)||tiene13){
		return true;
	}else{
		return false;
	}	
	}
}