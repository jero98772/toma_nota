import java.util.Scanner;
public class DeFront{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		String txt1 = input.nextLine();
		String txt1 = txt1.toLowerCase(); 
		String txt1SubString;
		if ("a".equals(txt1.charAt(0))){
			String txt1SubString = "a"+txt1.substring(2,txt1.length());
}		if ("b".equals(txt1.charAt(1))){
			String txt1SubString = txt1.substring(1,txt1.length());
}		else{
			String txt1SubString = txt1.substring(2,txt1.length());
}
		System.out.println(txt1SubString);
	}
}