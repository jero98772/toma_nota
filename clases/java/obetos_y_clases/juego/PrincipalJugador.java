import Jugador.Jugador;
import java.util.Scanner;
class PrincipalJugador{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        Jugador jugador = new Jugador();
        //System.out.println("bienvenido la tarea de java , cree su jugador");
        //System.out.println("introdusca la salud de su jugador");
        int salud = input.nextInt();
        jugador.setSalud(salud);
        //System.out.println("ingrse su nombre del estudiante/jugador");
        String nombre = input.next();//para moodle vpl se usa next y no nextLine
        jugador.setNombre(nombre);
        //System.out.println("¿cuantos talleres a hecho mal?");
        int ataque = input.nextInt();
        jugador.reducirSalud(ataque);
        //System.out.println("¿cuantos taller no entrego?");
        int ataque2  = input.nextInt();
        jugador.reducirSalud(ataque2);
        System.out.println(jugador.getNombre()+jugador.getSalud());
    }
}
