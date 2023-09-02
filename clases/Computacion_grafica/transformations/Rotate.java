package transformations;
import math.*;
import java.util.*;  

public class Rotate {
	public static ArrayList<points3> makeRotation(double rotateF,ArrayList<points3> dots){
		rotateF= Math.toRadians(rotateF);
		for(int i=0;i<dots.size();i++){
			points3 dot=dots.get(i);
		    int x = dot.getx();
            int y = dot.gety();

            double x2 = (double) x;
            double y2 = (double) y;

            double newx = Math.cos(rotateF) * x2 - Math.sin(rotateF) * y2;
            double newy = Math.sin(rotateF) * x2 + Math.cos(rotateF) * y2;

            dot.setx((int) newx);
            dot.sety((int) newy);
		}
		return dots;
	}
}
 
