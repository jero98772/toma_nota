package transformations;
import math.*;
import java.util.*;  

public class Zoom {
	public static ArrayList<points3> makeZoom(int zoomX,int zoomY,ArrayList<points3> dots){
		int[][] matrix = {
            {zoomX, 0, 0},
            {0, zoomY, 0},
            {0, 0, 1}
        };

		Matrix3x3 m = new Matrix3x3(matrix);

		for(int i=0;i<dots.size();i++){
			points3 dot=dots.get(i);
			//int x=dot.getx();
			//int y=dot.gety();
			points3 newd =m.times(dot);
			dots.set(i,newd);
			//dot.setx((int) (x * zoomF));
            //dot.sety((int) (y * zoomF));
			//System.out.println(x * zoomF);
			//System.out.println(y * zoomF);
		}
		return dots;
	}
}
 
