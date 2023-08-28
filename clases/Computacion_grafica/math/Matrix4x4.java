 
public class Matrix4x4 {
    private int[][] elements;

    public Matrix4x4(int[][] elements) {
        if (elements.length != 4 || elements[0].length != 4) {
            throw new IllegalArgumentException("Matrix must be 3x3");
        }
        this.elements = elements;
    }

    public int[][] getElements() {
        return elements;
    }

    public static points4 times(Matrix4x4 matrix, points4 point) {
        int[][] matrixElements = matrix.getElements();
        int x = matrixElements[0][0] * point.getx() + matrixElements[0][1] * point.gety() + matrixElements[0][2] * point.getz() + matrixElements[0][3] * point.getw();
        int y = matrixElements[1][0] * point.getx() + matrixElements[1][1] * point.gety() + matrixElements[1][2] * point.getz() + matrixElements[1][3] * point.getw();
        int z = matrixElements[2][0] * point.getx() + matrixElements[2][1] * point.gety() + matrixElements[2][2] * point.getz() + matrixElements[2][3] * point.getw();
        int w = matrixElements[3][0] * point.getx() + matrixElements[3][1] * point.gety() + matrixElements[3][2] * point.getz() + matrixElements[3][3] * point.getw();

        return new points4(x, y, z, w);
    }

    public static Matrix4x4 times(Matrix4x4 matrix1, Matrix4x4 matrix2) {
        int[][] elements1 = matrix1.getElements();
        int[][] elements2 = matrix2.getElements();
        int[][] resultElements = new int[3][3];

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
