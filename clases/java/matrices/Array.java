public class Array{
	public static int minimoBuscado(int[][] arr){
		int menor=arr[0][0];
			for(int i=0;i<arr.length;i++){
				for(int j=0;j<arr[0].length;j++){
				    if(menor<arr[i][j]){
					menor=arr[i][j];
				}
			}
		}
	return menor;
	}
}