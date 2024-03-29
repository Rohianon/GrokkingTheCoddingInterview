package twopointers;

import java.util.HashMap;

public class PairWithTargetSum2 {
    public static int[] search(int[] arr, int target) {
        HashMap<Integer, Integer> nums = new HashMap<>(); // Store numbers and indices
        for (int i = 0; i < arr.length; i++) {
            if (nums.containsKey(target - arr[i]))
                return new int[]{nums.get(target - arr[i]), i};
            else
                nums.put(arr[i], i); // put the number and its index in the map
        }
        return new int[]{-1, -1}; // pair not found
    }

    public static void main(String[] args) {
        int[] result = PairWithTargetSum2.search(new int[]{1, 2, 3, 4, 6}, 6);
        System.out.println("Pair with target sum: [" + result[0] + ", " + result[1] + "]");
        result = PairWithTargetSum.search(new int[]{2, 5, 9, 11}, 11);
        System.out.println("Pair with target sum: [" + result[0] + ", " + result[1] + "]");
    }
}
