import java.util.Scanner;
public class ExtraccionProfesional{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		String htmlCode = input.nextLine();
		String div1,div2,divClose,name,lastName;
		div1="<div class='name'>"
		div2="<div class='lastname'>"
		divClose="</div>"
		int indexNamePos1 = htmlCode.indexOf(div1)+div1.length();
		int indexNamePos2 = htmlCode.indexOf(divClose,indexNamePos1);
		int indexLastNamePos1 = htmlCode.indexOf(div2)+div2.length();
		int indexLastNamePos2 = htmlCode.indexOf(divClose,indexLastNamePos2);	
		String name = htmlCode.substring(indexNamePos1,indexNamePos2);
		String lastName = htmlCode.substring(indexLastNamePos1,indexLastNamePos2);
		System.out.println(name+lastName);
	}
}