public class x {
    public static void main(String[] args) {
        System.out.println("Cree un programa en Java que imprima el siguiente patrón:\n");
        System.out.println("11    11\n 11  11 \n  1111   \n 11  11\n11    11\n");
    }
    public static String[] Xdraw(String caracter, int medida) {
        //"tamaño" no es valido por el uso de la Ñ , no se vio nesario recurrir a una
        String caracterBlanco = " ".repeat(caracter.length());
        String[][] dibujo = new String[medida][medida];
        int x = 0;
        for(int i = 0;i<medida;i++){
            for(int j = 0;j<medida;j++){
                //x+1 = i , i-total
                //x = x+1, y =
                if(j == 4){
                    //test , = carcacter
                    dibujo[i][j] = caracter;
                }
                else{
                    dibujo[i][j] = caracterBlanco;
                }
            }
        }
    }
}
