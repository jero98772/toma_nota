fn main(){
	let mut xs=String::new();
	std::io::stdin().read_line(&mut xs).unwrap();
	let x : i32=xs.trim().parse().unwrap();
	if x%2==0{
		println!("is even");
	}else{
		println!("is odd");
	}
}
