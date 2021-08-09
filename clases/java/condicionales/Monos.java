public class Monos{
    boolean problemaMonos(boolean sonrie_a, boolean sonrie_b){
        boolean ambosMonos;
        if ((sonrie_a && sonrie_b) || !(sonrie_a && sonrie_b)){
            ambosMonos = true;
        }else{
            ambosMonos = false;
        }
        return ambosMonos;
    }
}
