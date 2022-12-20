package twopointers;

import java.util.Arrays;

public class RemoveDuplicates {
    public static int[] remove(int[] arr) {
        int nextNonDuplicate = 1; // index of the next non-duplicate element
        for (int i = 0; i < arr.length; i++) {
            if (arr[nextNonDuplicate - 1] != arr[i]) {
                arr[nextNonDuplicate] = arr[i];
                nextNonDuplicate++;
            }
        }
        return Arrays.copyOfRange(arr, 0, nextNonDuplicate);
    }

    public static void main(String[] args) {
        int[] arr = new int[]{2, 3, 3, 3, 6, 9, 9};
        System.out.println(Arrays.toString(RemoveDuplicates.remove(arr)));

        arr = new int[]{2, 2, 2, 11};
        System.out.println(Arrays.toString(RemoveDuplicates.remove(arr)));
    }
}
