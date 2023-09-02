package transformations;
import math.*;
import java.util.*;  

public class Move {
	public static ArrayList<points3> makeMove(int moveX,int moveY,ArrayList<points3> dots){
		for(int i=0;i<dots.size();i++){
			points3 dot=dots.get(i);
			int x=dot.getx();
			int y=dot.gety();
			dot.setx(x + moveX);
            dot.sety(y + moveY);
			System.out.println(x + moveX);
			System.out.println(y + moveY);
		}
		return dots;
	}
}
 
