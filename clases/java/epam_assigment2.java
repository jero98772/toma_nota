public class main {
    public static void main(String[] args) {
        int[] l=null;
        int m=maximumDistance(l);
        System.out.println(m);
    }
    public static int maximumDistance(int[] array) {
        if (array == null || array.length == 0) {
            return 0;
        }

        int max = array[0];
        int firstIndex = -1;
        int lastIndex = -1;

        // Find the maximum value
        for (int i = 0; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }

        // Find the first and last occurrence of the maximum value
        for (int i = 0; i < array.length; i++) {
            if (array[i] == max) {
                if (firstIndex == -1) {
                    firstIndex = i;
                }
                lastIndex = i;
            }
        }

        // Distance between the first and last occurrence
        return lastIndex - firstIndex;
    }
}
