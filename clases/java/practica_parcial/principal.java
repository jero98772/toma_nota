public class principal{
    public static void main(String[] args){
        personaje[] personajes=new personaje[4];
        hada h1=new hada("hadita1",10,10);
        hada h2=new hada("hadita2",20,20);
        elfo e1=new elfo("nn-1",10,10);
        elfo e2=new elfo("nn",20,20);
        personajes[0]=h1;
        personajes[1]=h2;
        personajes[2]=e1;
        personajes[3]=e2;
        personaje.mostrarNombresPersonajes(personajes);
    }
}
