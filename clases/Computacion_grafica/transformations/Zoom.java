package transformations;
import math.*;
import java.util.*;  

public class Zoom {
	public static ArrayList<points3> makeZoom(double zoomF,ArrayList<points3> dots){
		for(int i=0;i<dots.size();i++){
			points3 dot=dots.get(i);
			int x=dot.getx();
			int y=dot.gety();
			dot.setx((int) (x * zoomF));
            dot.sety((int) (y * zoomF));
			System.out.println(x * zoomF);
			System.out.println(y * zoomF);
		}
		return dots;
	}
}
 
