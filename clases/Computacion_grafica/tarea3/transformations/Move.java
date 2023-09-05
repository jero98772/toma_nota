package transformations;
import math.*;
import java.util.*;  

public class Move {
	public static ArrayList<points3> makeMove(int moveX,int moveY,ArrayList<points3> dots){
		int[][] matrix = {
            {1, 0, moveX},
            {0, 1, moveY},
            {0, 0, 1}
        };
		Matrix3x3 m = new Matrix3x3(matrix);
		for(int i=0;i<dots.size();i++){
			points3 dot=dots.get(i);
			points3 newd =m.times(dot);
			dots.set(i,newd);

		}
		return dots;
	}
}
 
