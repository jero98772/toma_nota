package math;

public class Matrix4x4 {
    public double [][] matrix = new double[4][4];

    public Matrix4x4() {
        // Create a 4x4 identity matrix
        matrix[0][0] = 1;   matrix[0][1] = 0;   matrix[0][2] = 0;   matrix[0][3] = 0;
        matrix[1][0] = 0;   matrix[1][1] = 1;   matrix[1][2] = 0;   matrix[1][3] = 0;
        matrix[2][0] = 0;   matrix[2][1] = 0;   matrix[2][2] = 1;   matrix[2][3] = 0;
        matrix[3][0] = 0;   matrix[3][1] = 0;   matrix[3][2] = 0;   matrix[3][3] = 1;
    }

    // Set the value of the matrix at row i, column j
    void set(int i, int j, double value) {
        matrix[i][j] = value;
    }

    // Multiply two 4x4 matrices
    public static Matrix4x4 times(Matrix4x4 m1, Matrix4x4 m2) {
        Matrix4x4 m3 = new Matrix4x4();
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j ++) {
                m3.matrix[i][j] = 0;
                for(int k = 0; k < 4; k++) {
                    m3.matrix[i][j] += m1.matrix[i][k] * m2.matrix[k][j];
                }
            }
        }
        return m3;
    }

    // Multiply a 4x4 matrix by a 4x1 vector
    public static Vector4 times(Matrix4x4 m, Vector4 v) {
        Vector4 v2 = new Vector4();
        for(int i = 0; i < 4; i++) {
            v2.vector[i] = 0;
            for(int j = 0; j < 4; j++) {
                v2.vector[i] += m.matrix[i][j] * v.vector[j];
            }
        }
        return v2;
    }
}