package math;
public class points3 {
    private int x;
    private int y;
    private int z;

    public points3(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public int getx() {
        return x;
    }

    public void setx(int x) {
        this.x = x;
    }

    public int gety() {
        return y;
    }

    public void sety(int y) {
        this.y = y;
    }

    public int getz() {
        return z;
    }

    public void setz(int z) {
        this.z = z;
    }

    @Override
    public String toString() {
        return "Value 1: " + x + ", Value 2: " + y + ", Value 3: " + z;
    }
}
 
