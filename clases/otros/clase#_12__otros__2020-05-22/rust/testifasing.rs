use std::io::stdin;
fn main(){
	let mut input=String::new();
	stdin().read_line(&mut input).unwrap();
	let x:i32=input.trim().parse().unwrap();
	let mut parity=String::new();
	if (x%2==0){
	 parity="even".to_string();
	}else{
	 parity="odd".to_string();
	}
	println!("{0}",parity);
}