public class IntArrayUtil {
    public static void swapEven(int[] array) {
             if (array == null || array.length <= 1) {
            // If array is empty or has only one element, no swaps needed
            return;
        }
        
        int left = 0;
        int right = array.length - 1;
        
        while (left < right) {
            if (array[left] % 2 == 0 && array[right] % 2 == 0) {
                // Both elements at left and right positions are even, swap them
                int temp = array[left];
                array[left] = array[right];
                array[right] = temp;
            }
            
            // Move to the next pair
            left++;
            right--;
        }
    }




    public static void main(String[] args) {
        // Test cases
        int[] array1 = {10, 5, 3, 4};
        swapEven(array1);
        printArray(array1); // Output: [4, 5, 3, 10]

        int[] array2 = {100, 2, 3, 4, 5};
        swapEven(array2);
        printArray(array2); // Output: [100, 4, 3, 2, 5]

        int[] array3 = {100, 2, 3, 45, 33, 8, 4, 54};
        swapEven(array3);
        printArray(array3); // Output: [54, 4, 3, 45, 33, 8, 2, 100]


    }

    // Utility method to print array
    private static void printArray(int[] array) {
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            if (i > 0) {
                System.out.print(", ");
            }
            System.out.print(array[i]);
        }
        System.out.println("]");
    }
}
