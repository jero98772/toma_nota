fn isdivisible(n:i32,m:i32)->bool{
	if n%m==0{
		return true;
	}else{
		return false;
	}
}
fn to_fizzbuzz(n:i32){
	match(isdivisible(n,3),isdivisible(n,5)){
		(true,true)=>println!("fizzbuzz"),
		(true,false)=>println!("fizz"),
		(false,true)=>println!("buzz"),	
		(false,false)=>println!("{n}"),
	}
}
fn main(){
	for i in 1..100{
		to_fizzbuzz(i);
	}
}