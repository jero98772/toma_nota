package math;
public class points4 {
    private int x;
    private int y;
    private int z;
    private int w;

    public points4(int x, int y, int z, int w) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.w = w;
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
    public int getw() {
        return w;
    }

    public void setw(int w) {
        this.w = w;
    }
    @Override
    public String toString() {
        return "Value 1: " + x + ", Value 2: " + y + ", Value 3: " + z;
    }
} 
