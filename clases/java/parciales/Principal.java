//import Carro
class Principal{
	public static void main(String[] args){
		Carro crr1 = new Carro("Tesla");
		Carro crr2 = new Carro("Mazda",false);
		crr1.aumentarVelocidad(10);
		crr2.aumentarVelocidad(40);
		System.out.printl(crr1.getVelocidad());
		System.out.printl(crr2.getVelocidad());
		crr2.encender();
		crr2.aumentarVelocidad(40);
		for(int i = 0 ;i<=3;i++){
			crr2.disminuirVelocidad(5);
		}
		System.out.printl(crr1.getVelocidad());
		System.out.printl(crr2.getVelocidad());
	}
}