package math;
 
public class Matrix3x3 {
    private int[][] elements;
    public void set(int[][] elements) {
        this.elements = elements;
    }
    public int getw() {
        return this.elements;
    }
    public Matrix3x3(int[][] elements) {
        if (elements.length != 3 || elements[0].length != 3) {
            throw new IllegalArgumentException("Matrix must be 3x3");
        }
        this.elements = elements;
    }

    public int[][] getElements() {
        return elements;
    }

    public  points3 times( points3 point) {
        int[][] matrixElements = this.elements;//matrix.getElements();
        int x = matrixElements[0][0] * point.getx() + matrixElements[0][1] * point.gety() + matrixElements[0][2] * point.getz();
        int y = matrixElements[1][0] * point.getx() + matrixElements[1][1] * point.gety() + matrixElements[1][2] * point.getz();
        int z = matrixElements[2][0] * point.getx() + matrixElements[2][1] * point.gety() + matrixElements[2][2] * point.getz();
        return new points3(x, y, z);
    }

    public  Matrix3x3 times(Matrix3x3 matrix1, Matrix3x3 matrix2) {
        int[][] elements1 = matrix1.getElements();
        int[][] elements2 = matrix2.getElements();
        int[][] resultElements = new int[3][3];

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
