fn main(){
	let mut name=String::new();
	println!("please insert your name");
	std::io::stdin().read_line(&mut name).unwrap();
	if name=="bob"{
		println!("welcome");
	}else{
		println!("{} not is welcome ",name);
	}	
}