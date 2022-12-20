package twopointers;

public class PairWithTargetSum {

    public static int[] search(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int currSum = arr[left] + arr[right];
            if (currSum == target)
                return new int[]{left, right}; // found the pair
            if (target > currSum)
                left++; // We need a pair with a bigger sum
            else
                right--;
        }
        return new int[]{-1, -1};
    }

    public static void main(String[] args) {
        int[] result = PairWithTargetSum.search(new int[]{1, 2, 3, 4, 6}, 6);
        System.out.println("Pair with target sum: [" + result[0] + ", " + result[1] + "]");
        result = PairWithTargetSum.search(new int[]{2, 5, 9, 11}, 11);
        System.out.println("Pair with target sum: [" + result[0] + ", " + result[1] + "]");
    }

}
