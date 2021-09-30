public class Array{
	public static int sumaDiagonal(int[][] arr){
		int diagonal=0;
			for(int i=0;i<arr.length;i++){
				for(int j=0;j<arr[0].length;j++){
					if(i==j){
						diagonal=diagonal+arr[i][j];
					}
				}
			}
		return diagonal;
	}