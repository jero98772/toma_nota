public class points3 {
    private double x;
    private double y;
    private double z;

    public points3(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public double getx() {
        return x;
    }

    public void setx(double x) {
        this.x = x;
    }

    public double gety() {
        return y;
    }

    public void sety(double y) {
        this.y = y;
    }

    public double getz() {
        return z;
    }

    public void setz(double z) {
        this.z = z;
    }

    @Override
    public String toString() {
        return "Value 1: " + x + ", Value 2: " + y + ", Value 3: " + z;
    }
}

 

public class points4 {
    private double x;
    private double y;
    private double z;
    private double w;

    public points4(double x, double y, double z, double w) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.w = w;
    }

    public double getx() {
        return x;
    }

    public void setx(double x) {
        this.x = x;
    }

    public double gety() {
        return y;
    }

    public void sety(double y) {
        this.y = y;
    }

    public double getz() {
        return z;
    }

    public void setz(double z) {
        this.z = z;
    }
    public double getw() {
        return w;
    }

    public void setw(double w) {
        this.w = w;
    }
    @Override
    public String toString() {
        return "Value 1: " + x + ", Value 2: " + y + ", Value 3: " + z;
    }
}
public class Matrix3x3 {
    private double[][] elements;
    
    public Matrix3x3(double[][] elements) {
        if (elements.length != 3 || elements[0].length != 3) {
            throw new IllegalArgumentException("Matrix must be 3x3");
        }
        this.elements = elements;
    }

    public double[][] getElements() {
        return elements;
    }

    public  points3 times(Matrix3x3 matrix, points3 point) {
        double[][] matrixElements = matrix.getElements();
        double x = matrixElements[0][0] * point.getx() + matrixElements[0][1] * point.gety() + matrixElements[0][2] * point.getz();
        double y = matrixElements[1][0] * point.getx() + matrixElements[1][1] * point.gety() + matrixElements[1][2] * point.getz();
        double z = matrixElements[2][0] * point.getx() + matrixElements[2][1] * point.gety() + matrixElements[2][2] * point.getz();
        return new points3(x, y, z);
    }

    public  Matrix3x3 times(Matrix3x3 matrix1, Matrix3x3 matrix2) {
        double[][] elements1 = matrix1.getElements();
        double[][] elements2 = matrix2.getElements();
        double[][] resultElements = new double[3][3];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                resultElements[i][j] = elements1[i][0] * elements2[0][j] +
                                       elements1[i][1] * elements2[1][j] +
                                       elements1[i][2] * elements2[2][j];
            }
        }

        return new Matrix3x3(resultElements);
    }

}


public class Matrix4x4 {
    private double[][] elements;

    public Matrix4x4(double[][] elements) {
        if (elements.length != 4 || elements[0].length != 4) {
            throw new IllegalArgumentException("Matrix must be 3x3");
        }
        this.elements = elements;
    }

    public double[][] getElements() {
        return elements;
    }

    public static points4 times(Matrix4x4 matrix, points4 point) {
        double[][] matrixElements = matrix.getElements();
        double x = matrixElements[0][0] * point.getx() + matrixElements[0][1] * point.gety() + matrixElements[0][2] * point.getz() + matrixElements[0][3] * point.getw();
        double y = matrixElements[1][0] * point.getx() + matrixElements[1][1] * point.gety() + matrixElements[1][2] * point.getz() + matrixElements[1][3] * point.getw();
        double z = matrixElements[2][0] * point.getx() + matrixElements[2][1] * point.gety() + matrixElements[2][2] * point.getz() + matrixElements[2][3] * point.getw();
        double w = matrixElements[3][0] * point.getx() + matrixElements[3][1] * point.gety() + matrixElements[3][2] * point.getz() + matrixElements[3][3] * point.getw();

        return new points4(x, y, z, w);
    }

    public static Matrix4x4 times(Matrix4x4 matrix1, Matrix4x4 matrix2) {
        double[][] elements1 = matrix1.getElements();
        double[][] elements2 = matrix2.getElements();
        double[][] resultElements = new double[3][3];

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                resultElements[i][j] = elements1[i][0] * elements2[0][j] +
                                       elements1[i][1] * elements2[1][j] +
                                       elements1[i][2] * elements2[2][j] +
                                       elements1[i][3] * elements2[3][j];
            }
        }

        return new Matrix4x4(resultElements);
    }

}

public class Vector3{
    private double x;
    private double y;
    private double z;

    public Vector3(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getZ() {
        return z;
    }

    public static Vector3 crossProduct(Vector3 v1, Vector3 v2) {
        double x = v1.getY() * v2.getZ() - v1.getZ() * v2.getY();
        double y = v1.getZ() * v2.getX() - v1.getX() * v2.getZ();
        double z = v1.getX() * v2.getY() - v1.getY() * v2.getX();
        return new Vector3(x, y, z);
    }

    public static double dotProduct(Vector3 v1, Vector3 v2) {
        return v1.getX() * v2.getX() + v1.getY() * v2.getY() + v1.getZ() * v2.getZ();
    }

    public double magnitude() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public Vector3 normalize() {
        double mag = magnitude();
        if (mag != 0) {
            return new Vector3(x / mag, y / mag, z / mag);
        }
        return new Vector3(0, 0, 0); // Cannot normalize a zero vector
    }


}

class Playground {
    public static void main(String[ ] args) {
        System.out.println("do something with the main");
    }
}