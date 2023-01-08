fn main(){
	let mut numstr=String::new();
	std::io::stdin().read_line(&mut numstr).unwrap();
	let num : i32=numstr.trim().parse().unwrap();
	let num1=num/100;
	let num2=((num/10)%10)*10;
	let num3=(num%10)*100;
	let newNum=num1+num2+num3;
	println!("{}",newNum)
}