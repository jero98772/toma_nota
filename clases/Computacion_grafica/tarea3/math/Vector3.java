package math;
public class Vector3{
    private int x;
    private int y;
    private int z;

    public Vector3(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int getZ() {
        return z;
    }

    public static Vector3 crossProduct(Vector3 v1, Vector3 v2) {
        int x = v1.getY() * v2.getZ() - v1.getZ() * v2.getY();
        int y = v1.getZ() * v2.getX() - v1.getX() * v2.getZ();
        int z = v1.getX() * v2.getY() - v1.getY() * v2.getX();
        return new Vector3(x, y, z);
    }

    public static int dotProduct(Vector3 v1, Vector3 v2) {
        return v1.getX() * v2.getX() + v1.getY() * v2.getY() + v1.getZ() * v2.getZ();
    }

    public int magnitude() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public Vector3 normalize() {
        int mag = magnitude();
        if (mag != 0) {
            return new Vector3(x / mag, y / mag, z / mag);
        }
        return new Vector3(0, 0, 0); // Cannot normalize a zero vector
    }


}
