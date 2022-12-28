fn main(){
	let mut name= String::new();
	println!("enter your name");
	std::io::stdin().read_line(&mut name).unwrap();
	println!("hello {}",name) 
}