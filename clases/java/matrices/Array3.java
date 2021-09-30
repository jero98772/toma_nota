public class Array{
	public static void transpuesta(int[][] arr){
		int[][] nuevaMatriz=new int [arr[0].length][arr.length];
			for(int i=0;i<arr.length;i++){
				for(int j=0;j<arr[0].length;j++){
				    nuevaMatriz[i][j]=arr[j][i];
					System.out.println(arr[j][i]);
				}
			}
		//System.out.println(nuevaMatriz);
	}
}